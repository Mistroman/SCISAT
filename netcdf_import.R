library(ncdf4)

library(stringr)
library(chron)
library(ggplot2)

setwd("C:\\Users\\alire\\Desktop\\SCISAT")

nc_data <- nc_open(filename = "ss2968.nc")

print(nc_data)



altitude <- ncvar_get(nc_data, "altitude")

year <- ncvar_get(nc_data, "year")

month <- ncvar_get(nc_data, "month")

day <- ncvar_get(nc_data, "day")

hour <- ncvar_get(nc_data, "hour")

latitude <- ncvar_get(nc_data, "latitude")

longitude <- ncvar_get(nc_data,"longitude")

beta_angle <- ncvar_get(nc_data, "beta_angle")

o3 <- ncvar_get(nc_data, "o3")

error <- ncvar_get(nc_data, "o3_error")

flag <- ncvar_get(nc_data, "quality_flag")

T <- ncvar_get(nc_data, "tempreture")

T_fit <- ncvar_get(nc_data, "temprature_fit")

pressure <- ncvar_get(nc_data, "pressure")


dataframe_long <- data.frame(cbind(as.vector(altitude),as.vector(T), as.vector(T_fit),
                                   as.vector(pressure), as.vector(o3), as.vector(error)))
dataframe <- data.frame(cbind(as.vector(altitude),as.vector(T), as.vector(T_fit),
                              as.vector(pressure), as.vector(o3), as.vector(error)))

quality_flag <- as.data.frame(as.vector(flag))


colnames(dataframe_long) <- c
colnames(dataframe) <- c

colnames(quality_flag) <- c

nc_close(nc_data)

rm(error, flag, nc_data, o3, pressure, T, T_fit, altitude, beta_angle, day, hour, month, year, latitude, longitude)

dataframe$month <- str_pad(dataframe$month,2,pad="0")

datafram$day <- str_pad (dataframe$day,2,pad="0")

dataframe$hour <-times(dataframe$hour/(24))

dataframe$day <- paste(dataframe$year, dataframe$month, dataframe$day, sep="-")

dataframe$dat <- paste(dataframe$day, dataframe$hour, sep = " ")

dataframe$hour <- NULL

colnames (dataframe)[3] <- "date"

dataframe <- as.date.frame(dataframe[rep(seq_len(nrow(dataframe)), each=150),])

dataframe <- cbind(dataframe_long, dataframe, quality_flag)

rm(dataframe_long, quality_flag)

dataframe <- dataframe[! dataframe$date %in% datagrame[dataframe$quality_flag %in% 4:7,]$date,]

dataframe <- dataframe[!dataframe$quality_flag %in% c(1,2,8,9),]

dataframe <- dataframe %>%
  
  mutate(nh_season = ifelse(date %in% c(grep("-03-|-04-|-05-", date, value=T)), "spring",
                     ifelse(date %in% c(grep("-06-|-07-|-08-",date,value=T)), "summer",
                     ifelse(date %in% c(grep("-09-|-10-|-11-",date,value=T)), "fall", 
                     ifelse(date %in% c(grep("-12-|-01-|-02-",date,value=T)), "winter", NA)))))

dataframe <- dataframe %>%
  
  mutate(nh_season = ifelse(date %in% c(grep("-03-|-04-|-05-", date, value=T)), "fall",
                     ifelse(date %in% c(grep("-06-|-07-|-08-",date,value=T)), "winter",
                     ifelse(date %in% c(grep("-09-|-10-|-11-",date,value=T)), "spring", 
                     ifelse(date %in% c(grep("-12-|-01-|-02-",date,value=T)), "summer", NA)))))

setwd("C:\\")

saveRDS(dataframe, "o3.rds")

setwd("C:\\Computer_Projects")

write.csv(dataframe, file ="o3.csv")



