# social-web-assignment

## Build a social media application that allows users to post messages and "like" other users' messages. 

## How to run the api

1. clone this repo 
2. make a virtul env
3. pip install -r requirements.txt

[visit this website for detail](https://alicecampkin.medium.com/setting-up-a-forked-django-project-53d5939b7e9e)

<hr>

### Here are some screenshots for clear demonstration- 

## 1. View list of all messages

 >> messages are ordered acc. to timestamp ie. latest message on the top </br>
 >> no. of likes of each msg is shown </br>
 >> users who likes the msg </br>
</br>

![Screenshot (74)](https://user-images.githubusercontent.com/72871727/212491281-2304a6b9-6743-4cf0-9f4b-81e7638c8f9b.png)

</br>

## 2. View a single message - MessageDetail 

>> requests - get, put, patch, delete</br>
</br>

![Screenshot (75)](https://user-images.githubusercontent.com/72871727/212491382-fac2c648-a37d-4974-977b-5c51d3fda653.png)

## 3. Like a message

>> msg 1, liked by user = shreya

![Screenshot (73)](https://user-images.githubusercontent.com/72871727/212491690-c1efcff6-d0c0-4175-9048-68c831c18ade.png)


</br>

>> if same user send request to like the same message again 

</br>

![Screenshot (79)](https://user-images.githubusercontent.com/72871727/212491774-2b44b838-8df4-4846-b2e8-ba144c7510fa.png)


</br>

## 4. Filter Messages

>> filter all msgs where sender= hp

![Screenshot (76)](https://user-images.githubusercontent.com/72871727/212491556-011d0db7-2e3a-407e-8ea0-c6ed7609fbb1.png)


<hr>

### Used PostgreSQL as db

>> SQL for - Message table

![Screenshot (77)](https://user-images.githubusercontent.com/72871727/212491911-ebbbb349-31cb-4dd9-82cf-f2709942870b.png)
</br>

>> SQL for - LikeMessage table

![Screenshot (78)](https://user-images.githubusercontent.com/72871727/212491917-46be063c-745c-419f-a401-d8cfa53e7a51.png)


 
 

