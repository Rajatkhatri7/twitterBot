# twitterBot

Now a days everything is going on automation .We live in the api world. A good example is the bots which we are using now a days . We see that on every website there is a Bot which helps in answering simple queries , they are smart enough. isn't it appears interesting to you . So in this repository I will we will make a twitter bot from scratch and later we will add more functionality in it. Follow the steps below.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Creating Twitter API Authentication Credentials

The Twitter API requires that all requests use OAuth to authenticate. So you need to create the required authentication credentials to be able to use the API. These credentials are four text strings:

1.Consumer key
2.Consumer secret
3.Access token
4.Access secret


## Step 0 Email Verification

First go to [Twitter](https://twitter.com) Signin withyour account and verify your email id by going to ...more >Setting and security >Email
Enter your email there there and then it will send a link to your gmail account . Go to your [gmail account](https://mail.google.com/) and click verify.

## Step 1 Apply for a Twitter Developer Account

Visit [Twitter Developer](https://developer.twitter.com/en) and click on Signin at top right corner.Here sign in with your twitter accaount.
Then after Signin Click on Apply at top right corner.

![apply image](https://files.realpython.com/media/dev_account_01.2a5eab8edcb8.png)

## Step 2 Apply for Bot

Click on create a bot if a window will appear to you.
Then click on continue and fill the all necessary details which it asking. Its quite booring its a long form but somOne says "Patience is the key to success" so keep patience and fill it.

## Step 3 Email verification again

After filling all the details it will ask for the email verification "Privacy matters" so again go to the [gmail account](https://mail.google.com/) and verify.

## Step 4 Creating the credintails

Now you will see your Name and Profile at top right corner. Click on the your name and from list click on Apps. In the next window click on create> You will see that it is asking for some details . For now we will fill the details only (required details) do not fill anthing where (required)is not written . In the website url section and callback url section  fillcopy this and paste https://consistant.netlify.app/ [Visit Website] (https://consistant.netlify.app/) this web is developed by me to stay consistant whole day. Tick mark the Enable signin with twitter, Fill the details and click on create.

## Step 5
 
 You will see a window like below. Click onKeys and tokens . You will see API KEY,API SECREAT key and for access and tokens Click on generate .A pop up will appear copy the access token and access token secreat becoz if u back it will not show to u. WE will use these token in python Script to create a bot.
