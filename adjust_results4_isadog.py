#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/adjust_results4_isadog.py
#                                                                             
# PROGRAMMER: Aditi Shelke
# DATE CREATED: 27 Nov 2023                      
# REVISED DATE: 
# PURPOSE: Create a function adjust_results4_isadog that adjusts the results 
#          dictionary to indicate whether or not the pet image label is of-a-dog, 
#          and to indicate whether or not the classifier image label is of-a-dog.
#          All dog labels from both the pet images and the classifier function
#          will be found in the dognames.txt file. We recommend reading all the
#          dog names in dognames.txt into a dictionary where the 'key' is the 
#          dog name (from dognames.txt) and the 'value' is one. If a label is 
#          found to exist within this dictionary of dog names then the label 
#          is of-a-dog, otherwise the label isn't of a dog. Alternatively one 
#          could also read all the dog names into a list and then if the label
#          is found to exist within this list - the label is of-a-dog, otherwise
#          the label isn't of a dog. 
#         This function inputs:
#            -The results dictionary as results_dic within adjust_results4_isadog 
#             function and results for the function call within main.
#            -The text file with dog names as dogfile within adjust_results4_isadog
#             function and in_arg.dogfile for the function call within main. 
#           This function uses the extend function to add items to the list 
#           that's the 'value' of the results dictionary. You will be adding the
#           whether or not the pet image label is of-a-dog as the item at index
#           3 of the list and whether or not the classifier label is of-a-dog as
#           the item at index 4 of the list. Note we recommend setting the values
#           at indices 3 & 4 to 1 when the label is of-a-dog and to 0 when the 
#           label isn't a dog.
#
##
# TODO 4: Define adjust_results4_isadog function below, specifically replace the None
#       below by the function definition of the adjust_results4_isadog function. 
#       Notice that this function doesn't return anything because the 
#       results_dic dictionary that is passed into the function is a mutable 
#       data type so no return is needed.
# 
def adjust_results4_isadog(results_dic, dogfile):
    dognames_dict = dict()

    # Reads in dognames from file,
    with open(dogfile, "r") as infile:
        # Reads in dognames 
        line = infile.readline()

 
        # processing line and adding dognames to dognames_dic with while loop
        while line != "":

            # TODO: 4a. REPLACE pass with CODE to remove the newline character
            #           from the variable line  
            #
            # Process line by striping newline from line
            # TODO: 4b. REPLACE pass with CODE to check if the dogname(line) 
            #          exists within dognames_dic, then if the dogname(line) 
            #          doesn't exist within dognames_dic then add the dogname(line) 
            #          to dognames_dic as the 'key' with the 'value' of 1. 
            #
            if line not in dognames_dict:
                dognames_dict[line.rstrip()] = 1

            # Reads in next line in file to be processed with while loop
            # if this line isn't empty (EOF)
            line = infile.readline()

                
    # Add to whether pet labels & classifier labels are dogs by appending
    # two items to end of value(List) in results_dic. 
    # List Index 3 = whether(1) or not(0) Pet Image Label is a dog AND 
    # List Index 4 = whether(1) or not(0) Classifier Label is a dog
    # How - iterate through results_dic if labels are found in dognames_dic
    # then label "is a dog" index3/4=1 otherwise index3/4=0 "not a dog"
    for key in results_dic:

        # Pet Image Label IS of Dog (e.g. found in dognames_dic)
        if results_dic[key][0] in dognames_dict:
            
            # Classifier Label IS image of Dog (e.g. found in dognames_dic)
            # appends (1, 1) because both labels are dogs
            if results_dic[key][1] in dognames_dict:
                results_dic[key].extend((1, 1))

            # TODO: 4c. REPLACE pass BELOW with CODE that adds the following to
            #           results_dic dictionary for the key indicated by the 
            #           variable key - append (1,0) to the value using 
            #           the extend list function. This indicates
            #           the pet label is-a-dog, classifier label is-NOT-a-dog. 
            #                              
            # Classifier Label IS NOT image of dog (e.g. NOT in dognames_dic)
            # appends (1,0) because only pet label is a dog
            else:
                results_dic[key].extend((1, 0))


        # Pet Image Label IS NOT a Dog image (e.g. NOT found in dognames_dic)
        else:
            # TODO: 4d. REPLACE pass BELOW with CODE that adds the following to
            #           results_dic dictionary for the key indicated by the 
            #           variable key - append (0,1) to the value uisng
            #           the extend list function. This indicates
            #           the pet label is-NOT-a-dog, classifier label is-a-dog. 
            #                              
            # Classifier Label IS image of Dog (e.g. found in dognames_dic)
            # appends (0, 1)because only Classifier labe is a dog
            if results_dic[key][1] in dognames_dict:
                results_dic[key].extend((0, 1))

            # TODO: 4e. REPLACE pass BELOW with CODE that adds the following to
            #           results_dic dictionary for the key indicated by the 
            #           variable key - append (0,0) to the value using the 
            #           extend list function. This indicates
            #           the pet label is-NOT-a-dog, classifier label is-NOT-a-dog. 
            #                                              
            # Classifier Label IS NOT image of Dog (e.g. NOT in dognames_dic)
            # appends (0, 0) because both labels aren't dogs
            else:
                results_dic[key].extend((0, 0))





    