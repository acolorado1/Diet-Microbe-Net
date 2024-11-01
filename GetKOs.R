# I need to create a file of KOs for each patient
library(readr)
library(dplyr)

all_genefamilies_ko <- read_delim("Data/SampleKOs/HoMI output/all_genefamilies_ko.tsv", 
                                  delim = "\t", escape_double = FALSE, 
                                  trim_ws = TRUE)
colnames(all_genefamilies_ko)[1] <- "GeneFamily"

# ZIM100 = Western 
we_sample <- all_genefamilies_ko %>% 
  select(GeneFamily, `ZIM100_Abundance-RPKs`) %>% 
  filter(`ZIM100_Abundance-RPKs` != 0) %>% 
  mutate(KO = substr(GeneFamily, 1, 6)) %>% 
  filter(substr(GeneFamily, 1, 1) == "K") %>% 
  select(KO) %>% 
  distinct()

write.table(we_sample, "/Users/burkhang/Code_Projs/Diet-Microbe-Net/Data/SampleKOs/western_sample.txt",
            append = FALSE, sep = "\n", dec = ".",
            row.names = F, col.names = F)
write.csv(we_sample, "/Users/burkhang/Code_Projs/Diet-Microbe-Net/Data/SampleKOs/western_sample.csv")


# ZIM091 = Agrarian 
ag_sample <- all_genefamilies_ko %>% 
  select(GeneFamily, `ZIM091_Abundance-RPKs`) %>% 
  filter(`ZIM091_Abundance-RPKs` != 0) %>% 
  mutate(KO = substr(GeneFamily, 1, 6)) %>% 
  filter(substr(GeneFamily, 1, 1) == "K") %>% 
  select(KO) %>% 
  distinct()

write.table(ag_sample, "/Users/burkhang/Code_Projs/Diet-Microbe-Net/Data/SampleKOs/agrarian_sample.txt",
            append = FALSE, sep = "\n", dec = ".",
            row.names = F, col.names = F)
write.csv(ag_sample, "/Users/burkhang/Code_Projs/Diet-Microbe-Net/Data/SampleKOs/agrarian_sample.csv")



combined_agrarian <- read_csv("Code_Projs/Diet-Microbe-Net/Data/Diet/organisms/agrarian/combined_agrarian.txt", 
                              col_names = FALSE)
ca <- combined_agrarian %>% 
  distinct()
colnames(ca) <- "KO"
write.csv(ca, "/Users/burkhang/Code_Projs/Diet-Microbe-Net/Data/Diet/organisms/agrarian/comb_ag.csv", 
          row.names = F)

combined_western<- read_csv("Code_Projs/Diet-Microbe-Net/Data/Diet/organisms/western/combined_western.txt", 
                              col_names = FALSE)
cw <- combined_western %>% 
  distinct()
colnames(cw) <- "KO"
write.csv(cw, "/Users/burkhang/Code_Projs/Diet-Microbe-Net/Data/Diet/organisms/western/comb_we.csv", 
          row.names = F)
