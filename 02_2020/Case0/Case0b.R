library(datasets)

#---- load data ----
data(cars)

View(cars)

plot(cars$speed, cars$dist)

scatter.smooth(x=cars$speed, y=cars$dist, main="Dist ~ Speed")



#---- model ------


#----- see theoretical vs empirical model ---- 


#---- mean absoulute percentage error ----

