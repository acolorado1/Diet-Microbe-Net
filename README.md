# Food Experiments for the Creation of Diet-Microbe Metabolic Networks

These are a collection of scripts, data, and notes that were used to better understand how different definitions of food items will result in different metabolic networks. 

## Installation

Utilizing the *env.yaml* file create a conda environment 

## Workflow 

- **Getting KOs**
  - First we had to identify which patients were eating the most Western vs Agrarian: this was done in *SampleIdentification.R*
  - Located in */Data/SampleKOs/* are two text files containing a list of KOs found in each sample 
    - This was performed by [HoMI](https://homi-pipeline.readthedocs.io/en/latest/)
    -  *GetKOs.R* was used to process HoMI outputs to make the tex files 
 -  **Getting Food Data**
    -  */Data/FooDB/*
       -  contains two text files with compounds associated with each diet 
       -  To recreate these files, download the [FooDB database CSVs](https://foodb.ca/downloads)
       -  Manually choose the food items 
       -  Run *FooDB_query.R* which takes in lists of food ids and will create dataframes of KEGG compound IDs linked to those food items
    -  */Data/organisms/* 
       -   contains two text files with the combined KOs queries from KEGG of the organisms representing each diet 
       -   to do this you can use one of AMON's functions and type: `extract_ko_genome_from_organism.py -i organism_id`
       -   preprocessing to get the unique list will have to be done (I did it through the command line)
      -   **for more information on this process see */notebooks/FoodToKEGG.md***
  -   **Running Analysis**
      -   Using food and sample data run [AMON](https://github.com/lozuponelab/AMON)
      -   Since AMON was not built exactly for our goal the */KEGG_mapper.tsv* file has to be processed: see *ProcessingKEGGmapper.py* 
      -   To create node and edge dataframes found in each experiment file (see *AMON_diettype/experiment*) run *main.py* from [co-metabolism network repo](https://github.com/acolorado1/Cometabolism-Network-Creation)
          -   You will need to make an accounut with Neo4j and make an instance where the URI, username, and password will be given to you
      -   Once in Neo4j run the following queries:
          -   To count nodes of certain origin: `MATCH p=({origin:'green'}) RETURN COUNT (p)`
          -   To find patterns: `MATCH p = ({origin: "blue"})<--(n) WHERE n.origin IN ["green", "yellow"] RETURN p`
          -   To find certain KOs: `MATCH (n)-[r:BECOMES]->(m) WHERE r.KOs = 'K15922' RETURN n, r, m`
      -   In Neo4j: once you get the pattern list you can convert output to *TABLE* format and download as a JSON file
          -   These outputs are labeled *patterns.json* in each experiments */Neo4j/* file
      -   Lastly using the scripts in the *PatternProcessing.py* file you can explore the unique KOs shared between experiments and output each diets *genelist.txt*  

## Notes

This is not an official pipeline nor has it been made modular (that is hopefully to come). 

Some of the files that are needed for network creation and output from AMON are also large and cannot be added to the repo. If you are interested in these please send me an email. 

## Contact

Angela Sofia Burkhart Colorado - angelasofia.burkhartcolorado@cuanschutz.edu