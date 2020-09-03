#!/bin/bash

scripts_dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
base_dir="$(dirname "$scripts_dir")"
raw_data_dir="$base_dir/raw_data"

for cname in $raw_data_dir/* ;
do
	class_dir_name="${cname##*/}"
	echo "class dir name $class_dir_name"
	urls_file="$raw_data_dir/$class_dir_name/urls_$class_dir_name.txt"
	#images_dir="$raw_data_dir/$cname/IMAGES"
	images_dir="$base_dir/IMAGES/$class_dir_name/"
	mkdir -p "$images_dir"
	echo "Class: $class_dir_name. Total # of urls: $(cat $urls_file | wc -l)"
	echo "Downloading images..."
	xargs -n 20 -P 8 wget -nc -q --timeout=5 --tries=2 -P "$images_dir" < "$urls_file"

	# url_file_name="${url_file##*/}"
	# file_extension="${url_file_name##*.}"
	# filename="${url_file_name%.*}"
	# urls_file="$source_urls_dir/$url_file_name"
	# echo "$urls_file"
	# images_dir="$base_dir/IMAGES/$filename"
    # mkdir -p "$images_dir"
	# echo "Class: $filename. Total # of urls: $(cat $urls_file | wc -l)"
	# echo "Downloading images..."
	# xargs -n 20 -P 8 wget -nc -q --timeout=5 --tries=2 -P "$images_dir" < "$urls_file"
done
