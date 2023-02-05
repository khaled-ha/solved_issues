import os
from typing import List
import shutil
import time
import filecmp
from checksumdir import dirhash
import logging
import argparse
 
parser = argparse.ArgumentParser()

# Adding optional argument
parser.add_argument("--LogFile", type=str, help = "LogFile")
parser.add_argument("--Interval_time", type=str, help = "time")
parser.add_argument("--Source", type=str, help = "source file")
parser.add_argument("--Replica", type=str, help = "replica file")

# Read arguments from command line
args = parser.parse_args()

if args.LogFile:
    print("Displaying LogFile as: % s" % args.LogFile)
    logging.basicConfig(filename=args.LogFile, filemode='w', format='%(name)s - %(levelname)s - %(message)s')
    logger = logging.getLogger(args.LogFile)
else:
    logger = logging.getLogger(__name__)


class FilePathDoesNotExist(Exception):
    def __init__(self, message, *args: object) -> None:
        super().__init__(message)


class Replica:
    def __init__(self, replica_path):
        if not os.path.exists(replica_path):
            logger.error('File does not exist')
            raise(FilePathDoesNotExist('folder path %s does not exist', replica_path))
        self.replica_path = replica_path


class Source:
    
    def __init__(self, source_path: str, replica: Replica, timer: int) -> None:
        if not os.path.exists(source_path):
            logger.error('File does not exist')
            raise(FilePathDoesNotExist('folder path %s does not exist', source_path))
        
        self.source_path = source_path
        self.replica = replica
        self.timer = timer

    def check_folder_matching_with_file_cmp(self) -> List:
        file_list_source = os.listdir(self.source_path)
        file_list_replica = os.listdir(self.replica.replica_path)
        to_be_removed_list = []
        for f in file_list_replica:
            if f not in file_list_source:
                to_be_removed_list.append(f)
        match, mismatch, errors = filecmp.cmpfiles(self.source_path, self.replica.replica_path, file_list_source, shallow = False,)
        # import ipdb;ipdb.set_trace()
        if errors:
            return errors, mismatch, to_be_removed_list
        if mismatch:
            return errors, mismatch, to_be_removed_list

        return [], [], to_be_removed_list

    def synchronize_based_on_file_cmp(self):
        while True:
            try:
                # import ipdb;ipdb.set_trace()
                errors, mismatch, remove_list = self.check_folder_matching_with_file_cmp()
                if errors and not mismatch:
                    for f in errors:
                        shutil.copy2(self.source_path + '/' + f , self.replica.replica_path + '/' + f)
                        logger.warning('created files %s', f)
                if mismatch and not errors:
                    for f in mismatch:
                        shutil.copy2(self.source_path + '/' + f , self.replica.replica_path + '/' + f)
                        logger.warning('copied files %s', f)
                if remove_list:
                    for f in remove_list:
                        os.remove(self.replica.replica_path + '/' + f)
                        logger.warning('remove file %s', f)
                time.sleep(self.timer)
            except Exception as e:
                logger.warning(e)
    
    
    def check_folder_matching_with_md5_hash(self):
        source_hash = dirhash(self.source_path)
        replica_hash = dirhash(self.replica.replica_path)
        return source_hash == replica_hash
    
    def synchronize_based_on_hash_cmp(self):
        while True:
            if not self.check_folder_matching_with_md5_hash():
                file_list_source = os.listdir(self.source_path)
                for f in file_list_source:
                    shutil.copy2(self.source_path + '/' + f , self.replica.replica_path + '/' + f)
            time.sleep(self.timer)

if __name__ == '__main__':
    # source_path = '/home/khaled/Desktop/veeam_test/dir1'
    # replica_path = '/home/khaled/Desktop/veeam_test/dir2'
    if args.Interval_time:
        timer = int(args.Interval_time)
    if args.Source:
        source_path = args.Source
    if args.Replica:
        replica_path = args.Replica
    replica = Replica(replica_path)
    source = Source(source_path, replica, timer)
    source.synchronize_based_on_file_cmp()

#This one to be used from command line
#python class\ Replica:.py --LogFile logfile.txt --Interval_time 1 --Source /home/khaled/Desktop/veeam_test/dir1 --Replica /home/khaled/Desktop/veeam_test/dir2