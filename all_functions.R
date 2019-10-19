library(sp)
library(rworldmap)
library(plyr)
library(dplyr)
library(chron)
library(ggplot2)
library(scales)

haversine <- function(lat1, lon1, lat2, lon2){
  2*(6371)*asin(sqrt((sin((lat2*pi/(180)-lat1*pi/(180))/2))^2 +
                       cos(lat1*pi/(180))*cos(lat2*pi/(180))*(sin((lon2*pi/(180)-lon1*pi/(180))/2))^2)) <= 500
  
}

have <- function(data, lat, lon){
  haversine <- function(lat1, lon1, lat2, lon2){
    2*(6371)*asin(sqrt((sin((lat2*pi/(180)-lat1*pi/(180))/2))^2 +
                         cos(lat1*pi/(180))*cos(lat2*pi/(180))*(sin((lon2*pi/(180)-lon1*pi/(180))/2))^2)) <= 200
    
    
  }
  subset(data, haversine(lat,lon,data$latitude, data$longitude))
  
}


data_filter <- function(data, datestring){
  data[grep(datestring, data$date),]
}


lat_lon_filtered <- function(data, min, max){
  data[data$latitude >=min & data$latitude <=max,]
  
}


column_dens <- function(data){
  number_dens <- function(ppm, column, p){
    R = 0.08205
    ppm*6.002*10^20*p/(R*column)
    
  }


  no_dens <- mapply(number_dens, ppm=data$o3, column = data$T, p = data$P_atm_)

  column <- data %>% mutate(col_dens = no_dens)

  column <- as.data.frame(column[,c(9,16)])
  column <- ddply(.data = column, .(date), numcolwise(sum))

  column$col_dens <- column$col_dens*1000

  column$dobson <- column$col_dens/(2.69*10^20)
}


coords2country = function(points){
  countriesSP <- getMap(resolution = 'low')
  
  pointsSP = SpatialPoints(points, proj4string = CRS(proj4string(countriesSP)))
  
  indices = over(pointsSP, countriesSP)
  
  indices$ADMIN
  
  
}

coords2continent = function(points){
  countriesSP <- getMap(resolution = 'low')
  
  pointsSP = SpatialPoints(points, proj4string = CRS(proj4string(countriesSP)))
  
  indices = over(pointsSP, countriesSP)
  
  indices$REGION

  
}

country_only <- function(data, country_name){
  subset(data, coords2country(data)==country_name)
}


avg <- function(data, column){
  ddply(.data = data, .(column), numclowise(mean))
}

city_mean <- function(data, lat, lon){
  ddply(.data = subset(data, haversine(lat,lon,data[,10], data[,11])), .(z), numcolwise(mean))
}


occultations <- function(data){
  df <- unique(data$date)
  nrow(df)
}







