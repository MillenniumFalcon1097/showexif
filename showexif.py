from utils import read_img_data, addMark, testraw
import argparse
import os

def parse_my_args():
    parser=argparse.ArgumentParser(description='Params')
    parser.add_argument('-imgdir',type=str,default="./imgs/",help="source image dir")
    parser.add_argument('-svdir',type=str,default="./outputs/",help="save dir")
    parser.add_argument('-tmpdir',type=str,default="./tmp/",help="temp dir, free to remove")
    parser.add_argument('-nocache',action="store_true",help="whether save the cached images for RAW convert.")
    args=parser.parse_args()
    return args


def preprocess(args):
    if not os.path.exists(args.svdir):
        os.mkdir(args.svdir)
    if not os.path.exists(args.tmpdir):
        os.mkdir(args.tmpdir)
    return

def clear_cache(args):
    tgt_dir=args.tmpdir
    cache_files=os.listdir(tgt_dir)
    for item in cache_files:
        os.remove(os.path.join(tgt_dir,item))
    print("All cached files have been removed!")
    return
    


if __name__=="__main__":
    # exif_data: [cam_factory, cam_name, shutterspd, aperture, iso, datetime, focallength]
    args=parse_my_args()
    preprocess(args)
    exif_list, img_list=read_img_data(args)
    addMark(args,exif_list,img_list)
    if args.nocache:
        clear_cache(args) 
