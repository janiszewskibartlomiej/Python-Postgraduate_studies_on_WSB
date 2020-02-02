library(dplyr)
library(caret)
library(e1071)
library(tree)
library(randomForest)
library(FSelector)

#----- load data ---- 
train <- read.csv(file="train.csv")
test <- read.csv(file="test.csv")





#----- prepare data -----

# check structure 
summary(train)
summary(test)

train <- train %>%
  mutate(Sex = as.factor(Sex), 
         NextAccident = as.factor(NextAccident))

test <- test %>%
  mutate(Sex = as.factor(Sex), 
         NextAccident = as.factor(NextAccident))







#----- build model(s) ------

# check inforamtion gain - feature selection
ChooseVar <- information.gain(NextAccident ~. , train)
ChooseVar

ChooseVar1 <- gain.ratio(NextAccident ~. , train )
ChooseVar1

ChooseVar2  <- symmetrical.uncertainty(NextAccident ~. , train)
ChooseVar2

cbind(ChooseVar, ChooseVar1, ChooseVar2)


### GLM MODEL
glm.fit <- glm(NextAccident ~  . ,
               data = train,
               family = binomial)

# check model summary

summary(glm.fit)


#choose variables for test dataset (must be the same as in train model)
# test1 <- test %>%
#   select(LicenseYear, 
#          CarBrand, 
#          CarEngine,
#          EngineCap,
#          CarValue)


# make predictions
glm.probs <- predict(glm.fit, test, type = "response")
glm.probs

# cut off level
results_lr <- ifelse(glm.probs < 0.6, "0", "1")
results_lr <- factor(results_lr, levels= c("0", "1"))


# validate / measure accuracy -  test data
glm_result <- confusionMatrix(results_lr, test1$NextAccident)
glm_result





### TREE MODEL

tree.fit <- tree(NextAccident ~ .,
                 data = train)


#choose variables for test dataset (must be the same as in train model)
# test1 <- test %>%
#   select(LicenseYear, 
#          CarBrand, 
#          CarEngine,
#          EngineCap,
#          CarValue)


# make predictions
results_tree <- predict(tree.fit, test, type = "class")




# validate / measure accuracy -  test data
tree_result <- confusionMatrix(results_tree, test1$NextAccident)
tree_result









### RANDOM FOREST
rf <- randomForest(NextAccident ~ .,
                   data = train)


#choose variables for test dataset (must be the same as in train model)
# test1 <- test %>%
#   select(LicenseYear, 
#          CarBrand, 
#          CarEngine,
#          EngineCap,
#          CarValue)

# make predictions

results_rf <- predict(rf, test)



# validate / measure accuracy -  test data
rf_result <- confusionMatrix(results_rf, test1$NextAccident)
rf_result


