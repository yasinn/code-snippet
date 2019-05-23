# -*- coding: utf-8 -*-

from __future__ import print_function
import os, sys
import oss2

#AccessKeyId and AccessKeySecret
auth = oss2.Auth('', '')

#Endpoint and Bucket
bucket = oss2.Bucket(auth, 'Endpoint', 'Bucket')

def percentage(consumed_bytes, total_bytes):
    if total_bytes:
        rate = int(100 * (float(consumed_bytes) / float(total_bytes)))
        print('\r{0}% '.format(rate), end='')
        sys.stdout.flush()

for root, dirs, files in os.walk('/mnt/www'):
    for file in files:
        p=os.path.join(root,file)
        print(p[4:])	
        # print(p[36:]) substring if needed, will remove unwanted path
        # /mnt/www/foo/bar/images/
        oss2.resumable_upload(bucket, '' + p[5:], p, progress_callback=percentage)
        
