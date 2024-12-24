CREATE TABLE Donor (
    DonorID int NOT NULL AUTO_INCREMENT,
    NameOfRestaurant varchar(255),
    EmailID varchar(255),
    PhoneNumber varchar(15),
    Address varchar(255),
    City varchar(50),
    State varchar(50),
    Pincode varchar(10),
    TypeOfCuisine varchar(100),
    OpenTime time,
    CloseTime time,
    PRIMARY KEY (DonorID)
);

INSERT INTO Donor VALUES
(1, 'Spice Delight', 'spicedelight@example.com', '+91 7517458889', '36, Spice Delight Street, Mumbai', 'Mumbai', 'Maharashtra', '110066', 'Indian Cuisine', '00:00:17', '00:00:21'),
(2, 'Green Garden', 'greengarden@example.com', '+91 9806871886', '58, Green Garden Street, Delhi', 'Delhi', 'New Delhi', '110057', 'Indian Cuisine', '00:00:08', '00:00:09'),
(3, 'Taste of India', 'tasteofindia@example.com', '+91 7069705473', '61, Taste of India Street, Bangalore', 'Bangalore', 'Karnataka', '110012', 'Indian Cuisine', '00:00:13', '00:00:18'),
(4, 'Cuisine Palace', 'cuisinepalace@example.com', '+91 7927626816', '62, Cuisine Palace Street, Chennai', 'Chennai', 'Tamil Nadu', '110069', 'Indian Cuisine', '00:00:12', '00:00:14'),
(5, 'Flavors of India', 'flavorsofindia@example.com', '+91 7991254926', '45, Flavors of India Street, Hyderabad', 'Hyderabad', 'Andhra Pradesh', '110093', 'Biryani', '00:00:15', '00:00:16'),
(6, 'Saffron Kitchen', 'saffronkitchen@example.com', '+91 8963108364', '49, Saffron Kitchen Street, Kolkata', 'Kolkata', 'West Bengal', '110031', 'Rice and Fish curry', '00:00:14', '00:00:17'),
(7, 'Curry House', 'curryhouse@example.com', '+91 8777945396', '45, Curry House Street, Ahmedabad', 'Ahmedabad', 'Gujrat', '110022', 'Indian Cuisine', '00:00:10', '00:00:15'),
(8, 'Masala Grill', 'masalagrill@example.com', '+91 9218129945', '69, Masala Grill Street, Pune', 'Pune', 'Maharashtra', '110010', 'Indian Cuisine', '00:00:14', '00:00:15'),
(9, 'Royal Biryani', 'royalbiryani@example.com', '+91 9345436673', '76, Royal Biryani Street, Jaipur', 'Jaipur', 'Rajasthan', '110088', 'Indian Cuisine', '00:00:12', '00:00:17'),
(10, 'Mango Tree', 'mangotree@example.com', '+91 8381984548', '89, Mango Tree Street, Lucknow', 'Lucknow', 'Uttar Pradesh', '110006', 'Indian Cuisine', '00:00:14', '00:00:16'),
(11, 'Chaat Corner', 'chaatcorner@example.com', '+91 9059879347', '51, Chaat Corner Street, Mumbai', 'Mumbai', 'Maharashtra', '110008', 'Indian Cuisine', '00:00:17', '00:00:20'),
(12, 'Rajputana Dining', 'rajputanadining@example.com', '+91 8747404590', '2, Rajputana Dining Street, Delhi', 'Delhi', 'New Delhi', '110048', 'Indian Cuisine', '00:00:09', '00:00:14'),
(13, 'Punjab Tadka', 'punjabtadka@example.com', '+91 9091180735', '99, Punjab Tadka Street, Bangalore', 'Bangalore', 'Karnataka', '110028', 'Indian Cuisine', '00:00:09', '00:00:10'),
(14, 'Southern Spice', 'southernspice@example.com', '+91 8740967014', '48, Southern Spice Street, Chennai', 'Chennai', 'Tamil Nadu', '110083', 'Indian Cuisine', '00:00:15', '00:00:20'),
(15, 'Naan Stop', 'naanstop@example.com', '+91 8233320793', '79, Naan Stop Street, Kolkata', 'Kolkata', 'West Bengal', '110041', 'Rice and Fish curry', '00:00:14', '00:00:18');