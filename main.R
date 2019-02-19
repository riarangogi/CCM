library("Rlinkedin")

client_id<-"7879dvv96ek1sk"
client_secret<-"4KC8s5TWnmedxBzN"
application_name<-"rival_BBD"

token<-inOAuth(application_name = application_name,consumer_key = client_id,
        consumer_secret = client_secret)
