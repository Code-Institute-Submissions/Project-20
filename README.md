# Full Stack Frameworks with Django
### Welcome to Kimchi Palace

[Kimchi Palace](https://kimchi-palace.herokuapp.com/)<br>
[My Github Page](https://github.com/suchan5/Project-4)

This website is designed and developed as an e-commerce website for the site owner to sell their home-made style Kimchi, and for the external users who are interested in buying their Kimchi.

It comprises of three main sections which are to view all the available products/Kimchis, to create reviews and leave comments, and to maku online payment to purchase the products/Kimchis upon siging up and logging in.


# Technologies used
* HTML5 - It was used to build the structure of the website.
* CSS3 - It was used to give design effects and style to the website. Also, media query was used for responsive design purpose.
* JavaScript - It was used to make the website more dynamic and interactive.
* Python + Django - Python was used to build the full-stack web application with a relational database.
* Postgres - Relational database, Postgres, was used for designing a database structure and store data.
* [Cloudinary](https://cloudinary.com/) - It was used for image uploading function. Images are stored in Cloudiary's cloud.
* [Stripe](https://stripe.com/) - It was used for online payment processing function.
* [Google Fonts](https://fonts.google.com/) - it was used for different typographies for design effects.
* [jQuery 3.5.1](https://jquery.com) - It was used to make it easier to use JavaScript.
* [Bootstrap 4.5.2](https://getbootstrap.com) - It was used for structure and style for the website with responsive design for different media sizes.
* [Font Awesome](https://fontawesome.com/) - It was used for concise and intuitive design effect with using icons.


# Data Structure
![Dara Structure](#)


# Structure of the website
[Wireframe](#)
#### Each pages are intuitive and interactive which makes it easier for users to explore the contents throughout the website.
##### 'Main' page 
'Main' page is the first page the users see when they access the domain address. Jumbotron and Kimchi image is used as background in order to give a direct idea of what this e-commerce website is selling. Also, a navbar located in the head of the page to guide users for navigations. A seach engine is available in the navbar that users can search for a product/kimchi they want to look for. Subnavbar is also located and accessble from every page that they can login at anytime to make purchases. 
##### 'All Kimchis' page
'All Kimchis' page is where all the products/Kimhis are available for viewing. Users can search by search terms or by filtering main ingredients using dropdown bar.
##### 'Kimchi Details' page
'Kimchi Details' page is where users can veiw the details of the product/Kimchi, such as price, main ingredients, manufactured date and other relevant specifications of the product/Kimchi. 'Continue Shopping' and 'Add to cart' buttons are located to make shopping easier for the users.
##### 'Shopping Cart' page (authentication required)
'Shopping Cart' page is where users can view thir products/Kimchis they put in for future purchases. Users can update the quantities of items in the shopping cart of delete by simply clicking the buttons. Also, 'Continue Shopping' and 'Add to cart' buttons are located to make shopping easier for the users.
##### 'My Purchases' (authentication required)
'My Purchases' page is where users view their history of past purchases. Upon checking out, users are redirected to this page and can see their purchases.
##### 'Reviews' page
'Reviews' page is where users can create, read, update, and delete their own reviews about the prodects/Kimchis. Users can also view all other reviews posted by other users to gather personal review about the products before making purchases.
##### 'Review Details' page
'Review Details' page is where users can view the detailed review by clicking from 'Reviews' page. Users can also leave a comment below the review to share information or ideas.
##### 'Authentication' pages - login, logout, signup 
Login, logout, SignUp pages can be accessed via subnavbar.


# UI/UX Design
This website is created with a focus on UI/UX that is:
1. Simple & clear :
- This is achieved by giving consistency in design throughout the website. Also, I gave enough spacing (padding and margin) for better readability of the contents.

2. Easy to use :
- Responsiveness : For example, font size is responsive to different device sizes so that users can use the website even on smaller devices.
- Placeholder, icons, buttons, flash messages are added to guide the users.

3. Presentable :
- A clean and theme-related image (Kimchi) was chosen and incorporated as the background to improve the overall design.
- To give the texts a better visibility over the white background, I have added a translucent grey box(in 'Reveiw details' page and authentication pages) so that the contents are more readable.
- Images are uniform in size and are not pixelated even in different media sizes.
- For colors, black and green were chosen as two main colours in order to give consistency in design.
- Preview images of the reviews are available on the 'Review Details' page for intuitive effects.


## Features and functions added for improved UI/UX

#### Navbar : 
- A navbar is added on the top of the website for users' direct access to each sections. 
- Navbar shows the link of two main pages ('All Kimchis' and 'Reviews') so that the user can access to view prducts/Kimchis, or to post a review and other users' review.
- Shopping cart is located in the navbar for users to access at anytime when they want to make purchases.
- Navbar is accessible from every page.

#### Sub-navbar :
- Sub-navbar is located right above the navbar with login, logout, and sign-up link. 
- A static message shows the status of login (if user is not logged in, it shows "Login to make purchase". If a user(for example, user1) logged in, it shows "Welcome user1")
- When a user is succesfully logged in, login link change to logout link. 
- When a user is succesfully logged in, SignUp link change to My Purchase link

#### Giving guidance :
- Upon actions of users(for example, creating, editing and deleting of the reviews or upon succesful checkout) a flash message appears to indicate that the action is performed succesfully (Flash messages disappear after some time).
- Shopping cart shows the numbers of items currently in the users' shopping cart. (The numbers of items in the shopping cart become 0 upon succesful checkout)
- 'Shopping cart' page shows a message "※ No items in your shopping cart" when empty
- 'My purchase' page shows a message "※No past puchases" when there is no history of purchass
- In shopping cart, it calcultes total amount for users according to the quantity they put in the cart. 

#### Search function :
- Users can search for the recipes with search terms.
- Users can use search terms irrelevant to the upper case or lower case.
- Results will be shown for both scenarios where the search term is in full or in partial strings.
- Placeholders give users an idea what to fill in the blanks in the search engine.
- Users can search with filter by Main Ingredients.
- A message located below the search engine in the 'All Kimchis' page shows how many search results are available.

#### Pictures of Kimchis can be enlarged :
- For 'All Kimchis' page, all the pictures of products/Kimchis can be enlarged upon mouseover to give users a better interactive experiences.

#### Preview of images when submitting reviews :
- When submitting or updating the reviews of their own, users can view the preview of the images that they are going to post or edit.

#### Commenting function :
- Users can freely leave a comment on the reviews to their own or to others to share opinions with other users .

#### Scroll to the top button:
- When the user scrolls down 200px from the top of the document, a button shows to enable the users to scroll back to the top.

#### Redirect :
- For example, in 'Reviews' page, users are redirected to the same review where they left off. For example, a user is trying to update his/her own review and cancel, she/he is redirecting back to the review. 


## Features left to be implemented
- 
