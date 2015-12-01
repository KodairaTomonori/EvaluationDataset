# Evaluation Dataset for Japanese Lexical Simplification

## Notes:
  Sentences selected from BCCWJ, so they are not published.  
  Here, program which extract sentence is published.  
  This program is made by Python 2.7 .  


## Procedure:
  git clone https://github.com/KodairaTomonori/EvaluationDataset  
  cd Script  
  python get\sent\_from\_BCCWJ.py xxxx/BCCWJ/SUW/  
  python extract\_sentence\_from\_location.py  


## other Notes:
  substitution ranking is in substitutes folder.  
  subs.csv: target word list   
  ave\_rank.csv and mle\_rank.csv: Substitutes in these file  is sorted by average score and MLE score.   
  Cmma is indicated different rank, and space is indicated same rank.  


---------------
  Affiliation:   
    Tokyo Metropolitan University   
      System Design - Komachi Lab  
  Name: Kodaira Tomonori  
  E-mail: kodaira-tomonori-at-ed.tmu.ac.jp  

---------------
