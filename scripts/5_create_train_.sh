#!/bin/bash

scripts_dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
base_dir="$(dirname "$scripts_dir")"
external_dir="/media/mikalackis/Transcend"
raw_data_dir="$external_dir/IMAGES"
images_data_dir="$external_dir/IMAGES"
data_dir="$base_dir/data"
train_dir="/media/mikalackis/3719d14c-5eaf-4c7a-8230-25219a0b08c7/train"
mkdir -p "$train_dir"

echo "Copying image to the training folder"
mkdir -p "$train_dir/nsfw"
for cname in $raw_data_dir/* ;
do
	#raw_data_class_dir="$raw_data_dir/$cname"
	class_dir_name="${cname##*/}"
	raw_data_class_dir="$images_data_dir/$class_dir_name"
	echo "raw_data_class_dir $raw_data_class_dir"
	if [[ -d "$raw_data_class_dir" ]]
	then
		#mkdir -p "$train_dir/$class_dir_name"
		find "$raw_data_class_dir" -type f \( -name '*.jpg' -o -name '*.jpeg' \) -print0 |
		while IFS= read -r -d '' jpg_f
		do
		    cp "$jpg_f" "$train_dir/nsfw/$(uuidgen).jpg"
			#rm "$jpg_f"
		done
	fi
done

echo "Removing corrupted images"
find "$train_dir" -type f -name '*.jpg' -print0 | 
while IFS= read -r -d '' jpg_f
do
    is_corrupted="$(convert "$jpg_f" /dev/null &> /dev/null; echo $?)"
	if [[ "$is_corrupted" -eq  "1" ]]
	then
		echo "removing: $jpg_f"
		rm "$jpg_f"
	fi
done

echo "Removing very large (>10M) and very small (<6K) images"
find "$train_dir" -type 'f' -size +10M -delete
find "$train_dir" -type 'f' -size -6k -delete

echo "Number of files per class:"
for subdir in $(ls "$train_dir")
do 
	echo "$subdir": "$(find "$train_dir/$subdir" -type f | wc -l)"
done