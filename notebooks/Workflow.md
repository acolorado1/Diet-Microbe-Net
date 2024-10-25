# From Food to KEGG compounds

Here I will be documenting how I characterized a Western and Agrarian diet to be used in my diet-microbe network. Overall the goal of this work is to go from a food item to compounds that can be found in KEGG. 

**Compound**: this will include macro and micronutrients as well as small molecules (often referred to as non-nutrients).

There are three main ways of addressing this problem: 

1. Querying a metabolomincs database (e.g. **FooDB**)
2. Querying KEGG for all KOs (genes) associated with a food item and predicting compounds that will originate from them. 
3. MICOM has curated a list of compounds they associated with a Western and a high-fiber diet

## FooDB

### Identifying Foods

There are no exact matches for food items in FooDB. For example, when searching for *apple* there are 8 or more matches including: pineapple, custard apple, Wax apple, Crab apple, etc.

Therefore foods must be searched for and manually chosen for the diet. Here I defined my diets as the following. 

| Food | Diet | Food Type | Food ID |
| -------- | ------- | ---------- |----|
| Milk (Cow) | Agrarian | Dairy | 632 |
| Butter | Western | Dairy | 667 |
| Cheese | Western | Dairy | 631 |
| Grape | Agrarian | Fruit | 374 | 
| Orange | Agrarian | Fruit | 57 | 
| Carrot | Agrarian | Vegetable | 245 | 
| Sweet Potato | Agrarian | Vegetable | 92 |
| Chicken | Agrarian | Protein | 334 |
| Beef | Western | Protein | 506 | 
| Eggs | Western | Protein | 633 |
| Corn | Agrarian | Grain | 205 | 
| Bread | Western | Grain | 836 | 
| Rice | Western  | Grain | 125 |

*Note*: These food items were classified as Western or Agrarian by a nutritionist at the University of Colorado Anszhutz Medical Campus. See *Burkhart-Colorado et al. 2024 Microbiome 12, 18* for further information about this cohort and food frequency questionnaire. 

### FooDB downloads 

When downloading the database it will provide a lot of unneeded information for this task. The 3 spreadsheets that I will need are: Food, Content, and Compound External Descriptors. 

- **Food** will provide the Food ID in the **id** column 
- **Content** will have **food_id** column and **source_id** column which will correspond to a compound
- **Compound External Descriptor** will have **compound_id** and **external_id** which in some cases will have KEGG compound IDs (e.g. C0####)

### Results 

After finding all compounds with external descriptions linking to KEGG this yielded: 

| Diet | Total # of Compounds | 
| ----- | ------------| 
| Agrarian | 322 | 
| Western | 227 | 

Some classification of compounds was the following: 

|Super Class | # of Agrarian | # of Western |  
|--------------|--------------|----------|
| Alkaloids and derivatives | 10 | 10 |
| Benzenoids | 83 | 37 | 
|Homogeneous metal compounds | 32 | 14 
| Homogeneous non-metal compounds | 18 | 14 | 
|  Hydrocarbon derivatives | 1 | 1 | 
| Hydrocarbons | 4 | 0 | 
|Lignans, neolignans and related compounds| 2 | 0 |
| Lipids and lipid-like molecules | 395 | 191 | 
|Mixed metal/non-metal compounds|3|3|
|Nucleosides, nucleotides, and analogues|43|35|
|Organic acids and derivatives|130|80|
|Organoheterocyclic compounds|69|46|
|Organometallic compounds|1|1|
|Organonitrogen compounds|22|17|
|Organooxygen compounds|124|75|
|Organophosphorus compounds|5|4|
|Organosulfur compounds|7|3|
|Phenylpropanoids and polyketides| 100 |63|

## KEGG KOs 

Through the KEGG API one can query KEGG and get all organism associated KOs. Tools like AMON can then be used to predict compounds that may be involved in metabolism based on these KOs. 

Here I will define my diets as the following: 

- **Western**: cow (bta), pork (ssc), bread wheat (taes), and japanese rice (osa)
- **Agrarian**: grape (vvi), carrot (dcr), chicken (gga), corn (zma)

I have also cross referenced these organisms with the ones in FooDB to ensure that there is consistency between species. For example, I will not be comparing different different species of rice or corn. 