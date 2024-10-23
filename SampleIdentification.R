# This script will be used to determine which samples to use to create a representative 
# Western and Agrarian network from the 285 samples 

# needed packages
library(readr)
library(dplyr)
library(tidyverse)

# load in the data
Zim_Metadata_285 <- read_csv("Data/Zim_Metadata_285.txt")

# Find patient with the max and min WA_difference

## This patient: cohort A, Urban, WA_diff = 33, visit 2
max <- Zim_Metadata_285 %>% slice_max(WA_Difference) %>% 
  select(SampleID, PID, Cohort_Short, Arm_Short, WA_Difference, Visit,
         Total_Dairy:Total_Score)

## This patient: cohort A, Urban, WA_diff = -25, visit 2 
min <- Zim_Metadata_285 %>% slice_min(WA_Difference)%>% 
  select(SampleID, PID, Cohort_Short, Arm_Short, WA_Difference, Visit,
         Total_Dairy:Total_Score)

# Find out what total scores for food categories looks like and compare
max_totals <- max %>% 
  dplyr::select(PID, WA_Difference, contains("Total")) 

min_totals <- min %>% 
  dplyr::select(PID, WA_Difference, contains("Total")) 

compare_totals <- rbind(max_totals, min_totals)
