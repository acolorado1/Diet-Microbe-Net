packages <- c("readr", "dplyr")

for (package in packages) {
  if(!require(package, character.only = T)){
    install.packages(package)
    library(package)
  }
}

# load in data 
foods <- read_csv("Code_Projs/Diet-Microbe-Net/Data/foodb_2020_04_07_csv/Food.csv")
Content <- read_csv("Code_Projs/Diet-Microbe-Net/Data/foodb_2020_04_07_csv/Content.csv")
CExtDes <- read_csv("Code_Projs/Diet-Microbe-Net/Data/foodb_2020_04_07_csv/CompoundExternalDescriptor.csv")

# get foods that parially match the source 
subset <- foods %>% 
  filter(grepl("Rice", name))

# Food IDs that are needed 
agrarian_id <- c(632, 374, 57, 245, 92, 334, 205)
western_id <- c(667, 631, 506, 633, 836, 125)

# verify that there is content for each food item vector
agrarian_id_verified <- agrarian_id %in% Content$food_id
western_id_verified <- western_id %in% Content$food_id

# TODO: wrap with if statement to make sure verified is all true

# Get compound IDs, I believe these are labeled as the Source IDs in the contents file
agrarian_content <- Content[Content$food_id %in% agrarian_id, ]
western_content<-  Content[Content$food_id %in% western_id, ]

agrarian_comp_ids <- unique(agrarian_content$source_id)
western_comp_ids <- unique(western_content$source_id)

# get external descriptors 
ag_extDes <- CExtDes[CExtDes$compound_id %in% agrarian_comp_ids, ]
we_extDes <- CExtDes[CExtDes$compound_id %in% western_comp_ids, ]

ag_extDes <- ag_extDes %>% 
  select(external_id, compound_id) %>% 
  na.omit()

ag_KEGG <- unique(ag_extDes$external_id[grepl("^C[0-9]{5}$", CExtDes$external_id)])
ag_KEGG_comp <- ag_extDes[ag_extDes$external_id %in% ag_KEGG, ]
