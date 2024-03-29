#!/bin/bash

# 原始数据
train_data_path ./data/raw/train.txt

# demo数据
train_data_path ./data/demo/train_demo.txt

# mini-demo数据
train_data_path ./data/mini-demo/mini_demo.txt


# start pserver0
python train.py \
    --train_data_path ./data/mini-demo/mini_demo.txt \
    --is_local 0 \
    --role pserver \
    --endpoints 127.0.0.1:6000,127.0.0.1:6001 \
    --current_endpoint 127.0.0.1:6000 \
    --trainers 2 \
    > pserver0.log 2>&1 &

# start pserver1
python train.py \
    --train_data_path ./data/mini-demo/mini_demo.txt \
    --is_local 0 \
    --role pserver \
    --endpoints 127.0.0.1:6000,127.0.0.1:6001 \
    --current_endpoint 127.0.0.1:6001 \
    --trainers 2 \
    > pserver1.log 2>&1 &

# start trainer0
python train.py \
    --train_data_path ./data/mini-demo/mini_demo.txt \
    --is_local 0 \
    --role trainer \
    --endpoints 127.0.0.1:6000,127.0.0.1:6001 \
    --trainers 2 \
    --trainer_id 0 \
    > trainer0.log 2>&1 &

# start trainer1
python train.py \
    --train_data_path ./data/mini-demo/mini_demo.txt \
    --is_local 0 \
    --role trainer \
    --endpoints 127.0.0.1:6000,127.0.0.1:6001 \
    --trainers 2 \
    --trainer_id 1 \
    > trainer1.log 2>&1 &
