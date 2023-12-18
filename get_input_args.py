#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_input_args.py
#                                                                             
# PROGRAMMER: Aditi Shelke
# DATE CREATED:  27 Nov 2023                                 
# REVISED DATE: 
# PURPOSE: Create a function that retrieves the following 3 command line inputs 
#          from the user using the Argparse Python module. If the user fails to 
#          provide some or all of the 3 inputs, then the default values are
#          used for the missing inputs. Command Line Arguments:
#     1. Image Folder as --dir with default value 'pet_images'
#     2. CNN Model Architecture as --arch with default value 'vgg'
#     3. Text File with Dog Names as --dogfile with default value 'dognames.txt'
#
##
# Imports python modules
import argparse
def get_input_args():

    # Create Parse using ArgParser
    parser= argparse.ArgumentParser()
    parser.add_argument('--dir', type=str, default='pet_images/', 
                        help='Path to pet images')
    parser.add_argument('--arch', default='vgg',
                  help=' CNN model architecture')
    parser.add_argument('--dogfile', default='dognames.txt',
                  help='Path to text file w dog names')
    return parser.parse_args()
