#!/bin/bash

scripts_dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
base_dir="$(dirname "$scripts_dir")"
data_dir="$base_dir/data"
raw_data_dir="$base_dir/raw_data"

N=2000

train_dir="$data_dir/train"
test_dir="$data_dir/test"
mkdir -p "$test_dir"

for cname in $raw_data_dir/* ;
do
	class_dir_name="${cname##*/}"
	test_dir_class="$test_dir/$class_dir_name"
	mkdir -p "$test_dir_class"
	train_dir_class="$train_dir/$class_dir_name"
	ls "$train_dir_class" | shuf -n $N | xargs -I{} mv "$train_dir_class/{}" "$test_dir_class"
done

echo "Number of files per class (train):"
for subdir in $(ls "$train_dir")
do
	echo "$subdir": "$(find "$train_dir/$subdir" -type f | wc -l)"
done

echo "Number of files per class (test):"
for subdir in $(ls "$test_dir")
do
	echo "$subdir": "$(find "$test_dir/$subdir" -type f | wc -l)"
done