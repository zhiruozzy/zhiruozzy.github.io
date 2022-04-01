x=0
y=0
shousuo=int (input("请输入xx"))

shuzhang=int (input("请输入xx"))
if(shousuo>=140)and(shuzhang<90):
    print("单纯收缩期高血压")


if (shousuo<120):
   x=1
elif(shousuo>120)and(shousuo<139):
   x=2
elif(shousuo>140)and(shousuo<159):
   x=3
elif(shousuo>160)and(shousuo<179):
    x=4
elif(shousuo>=140):
   x=5

 
  