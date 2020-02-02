library(dplyr)
library(tree)
library(randomForest)
library(caret)
library(e1071)

#---- read data ----
clients_data <- read.table(file = "clients.txt", 
                           sep = ",", 
                           header = TRUE)


#---- prepare data -----


# split data:
set.seed(101)
alpha     <- 0.7 # percentage of training set
inTrain   <- sample(1:nrow(clients_data), alpha * nrow(clients_data))
train <- clients_data[inTrain,]
test  <- clients_data[-inTrain,]


summary(train)
summary(test)

train <- train %>%
  select(-numer) %>%
  mutate(plec = as.factor(plec),
         wysylka_oferty = as.factor(wysylka_oferty),
         zakup = as.factor(zakup)) 



test <- test %>%
  select(-numer) %>%
  mutate(plec = as.factor(plec),
         wysylka_oferty = as.factor(wysylka_oferty),
         zakup = as.factor(zakup)) 





#----- build model(s) ------
# check inforamtion gain - feature selection
ChooseVar <- information.gain(zakup ~. , train)
ChooseVar

ChooseVar1 <- gain.ratio(zakup ~. , train )
ChooseVar1

ChooseVar2  <- symmetrical.uncertainty(zakup ~. , train)
ChooseVar2

cbind(ChooseVar, ChooseVar1, ChooseVar2)



#### GLM MODEL ####

glm.fit <- glm(zakup ~ . ,
               data = train,
               family = binomial)

# check model summary

summary(glm.fit)

# test1 <- test %>%
#   select(.)


# make predictions
glm.probs <- predict(glm.fit, test, type = "response")
glm.probs

# cut off level
results_lr <- ifelse(glm.probs < 0.6, "0", "1")
results_lr <- factor(results_lr, levels= c("0", "1"))

# validate / measure accuracy - test data

glm_result <- confusionMatrix(results_lr, test$zakup)
glm_result











#### TREE MODEL ####

tree.fit <- tree(zakup ~ .,
                 data = train)



# test1 <- test %>%
#   select(.)

# make prediction

results_tree <- predict(tree.fit, test, type = "class")


# validate / measure accuracy - test data

### TREE
tree_result <- confusionMatrix(results_tree, test$zakup)
tree_result









#### RANDOM FOREST ####

rf <- randomForest(zakup ~ .,
                   data = train)


# test1 <- test %>%
#   select(.)

results_rf <- predict(rf, test)

# validate / measure accuracy - test data

rf_result <- confusionMatrix(results_rf, test$zakup)
rf_result








