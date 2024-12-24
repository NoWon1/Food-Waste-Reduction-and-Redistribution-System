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

INSERT INTO Donor VALUES
(16, 'Golden Curry', 'goldencurry@example.com', '+91 9234658723', '23, Golden Curry Street, Jaipur', 'Jaipur', 'Rajasthan', '110088', 'Indian Cuisine', '00:00:12', '00:00:17'),
(17, 'Spice Lounge', 'spicelounge@example.com', '+91 9827364512', '34, Spice Lounge Street, Delhi', 'Delhi', 'New Delhi', '110057', 'Indian Cuisine', '00:00:10', '00:00:15'),
(18, 'Taste Paradise', 'tasteparadise@example.com', '+91 9182736452', '56, Taste Paradise Street, Pune', 'Pune', 'Maharashtra', '110010', 'Indian Cuisine', '00:00:13', '00:00:18'),
(19, 'Heritage Biryani', 'heritagebiryani@example.com', '+91 9081726354', '72, Heritage Biryani Street, Hyderabad', 'Hyderabad', 'Andhra Pradesh', '110093', 'Biryani', '00:00:14', '00:00:19'),
(20, 'Royal Curry House', 'royalcurryhouse@example.com', '+91 8127364523', '88, Royal Curry House Street, Bangalore', 'Bangalore', 'Karnataka', '110028', 'Indian Cuisine', '00:00:09', '00:00:14'),
(21, 'Urban Spice', 'urbanspice@example.com', '+91 8991236754', '101, Urban Spice Street, Chennai', 'Chennai', 'Tamil Nadu', '110083', 'Indian Cuisine', '00:00:11', '00:00:15'),
(22, 'Desi Masala', 'desimasala@example.com', '+91 8876543210', '12, Desi Masala Street, Kolkata', 'Kolkata', 'West Bengal', '110041', 'Rice and Fish curry', '00:00:14', '00:00:18'),
(23, 'The Curry Spot', 'thecurryspot@example.com', '+91 9345126789', '67, The Curry Spot Street, Ahmedabad', 'Ahmedabad', 'Gujrat', '110022', 'Indian Cuisine', '00:00:14', '00:00:17'),
(24, 'Tandoor Tales', 'tandoortales@example.com', '+91 9183745620', '98, Tandoor Tales Street, Lucknow', 'Lucknow', 'Uttar Pradesh', '110006', 'Indian Cuisine', '00:00:16', '00:00:20'),
(25, 'Street Spice', 'streetspice@example.com', '+91 9876543211', '32, Street Spice Street, Jaipur', 'Jaipur', 'Rajasthan', '110088', 'Indian Cuisine', '00:00:10', '00:00:14'),
(26, 'Curry Kingdom', 'currykingdom@example.com', '+91 8736452198', '44, Curry Kingdom Street, Mumbai', 'Mumbai', 'Maharashtra', '110066', 'Indian Cuisine', '00:00:14', '00:00:18'),
(27, 'Flavors Junction', 'flavorsjunction@example.com', '+91 8675423981', '15, Flavors Junction Street, Bangalore', 'Bangalore', 'Karnataka', '110028', 'Indian Cuisine', '00:00:13', '00:00:15'),
(28, 'The Tandoori Table', 'tandooritable@example.com', '+91 8654231974', '29, Tandoori Table Street, Chennai', 'Chennai', 'Tamil Nadu', '110069', 'Indian Cuisine', '00:00:12', '00:00:17'),
(29, 'Biryani Bazaar', 'biryanibazaar@example.com', '+91 8543219876', '63, Biryani Bazaar Street, Kolkata', 'Kolkata', 'West Bengal', '110031', 'Biryani', '00:00:15', '00:00:19'),
(30, 'Curry Carnival', 'currycarnival@example.com', '+91 8452198763', '19, Curry Carnival Street, Ahmedabad', 'Ahmedabad', 'Gujrat', '110022', 'Indian Cuisine', '00:00:09', '00:00:14'),
(31, 'Spices of South', 'spicesofsouth@example.com', '+91 8345672910', '102, Spices of South Street, Hyderabad', 'Hyderabad', 'Andhra Pradesh', '110093', 'Rice and Fish curry', '00:00:14', '00:00:18'),
(32, 'Masala Delight', 'masaladelight@example.com', '+91 8217364598', '65, Masala Delight Street, Pune', 'Pune', 'Maharashtra', '110010', 'Indian Cuisine', '00:00:12', '00:00:17'),
(33, 'Biryani Junction', 'biryanijunction@example.com', '+91 8123948576', '88, Biryani Junction Street, Jaipur', 'Jaipur', 'Rajasthan', '110088', 'Biryani', '00:00:14', '00:00:19'),
(34, 'Spice Corner', 'spicecorner@example.com', '+91 8076543219', '54, Spice Corner Street, Mumbai', 'Mumbai', 'Maharashtra', '110066', 'Indian Cuisine', '00:00:10', '00:00:14'),
(35, 'Authentic Biryani', 'authenticbiryani@example.com', '+91 8967452319', '18, Authentic Biryani Street, Chennai', 'Chennai', 'Tamil Nadu', '110083', 'Biryani', '00:00:14', '00:00:19'),
(36, 'Saffron Bowl', 'saffronbowl@example.com', '+91 8654397210', '29, Saffron Bowl Street, Delhi', 'Delhi', 'New Delhi', '110048', 'Indian Cuisine', '00:00:12', '00:00:15'),
(37, 'Southern Curries', 'southerncurries@example.com', '+91 8074593126', '39, Southern Curries Street, Hyderabad', 'Hyderabad', 'Andhra Pradesh', '110093', 'Rice and Fish curry', '00:00:15', '00:00:20'),
(38, 'Tikka Tales', 'tikkatales@example.com', '+91 8671234598', '72, Tikka Tales Street, Bangalore', 'Bangalore', 'Karnataka', '110028', 'Indian Cuisine', '00:00:10', '00:00:16'),
(39, 'Masala Craft', 'masalacraft@example.com', '+91 8567391240', '58, Masala Craft Street, Kolkata', 'Kolkata', 'West Bengal', '110041', 'Indian Cuisine', '00:00:14', '00:00:19'),
(40, 'Curry Sutra', 'currysutra@example.com', '+91 8321459870', '76, Curry Sutra Street, Jaipur', 'Jaipur', 'Rajasthan', '110088', 'Indian Cuisine', '00:00:14', '00:00:18'),
(41, 'Tandoor Junction', 'tandoorjunction@example.com', '+91 8264597218', '94, Tandoor Junction Street, Chennai', 'Chennai', 'Tamil Nadu', '110083', 'Biryani', '00:00:13', '00:00:17'),
(42, 'Flavor Fiesta', 'flavorfiesta@example.com', '+91 8956217340', '20, Flavor Fiesta Street, Ahmedabad', 'Ahmedabad', 'Gujrat', '110022', 'Indian Cuisine', '00:00:12', '00:00:16'),
(43, 'North Spice', 'northspice@example.com', '+91 8143729561', '44, North Spice Street, Lucknow', 'Lucknow', 'Uttar Pradesh', '110006', 'Indian Cuisine', '00:00:14', '00:00:18'),
(44, 'Coastal Delight', 'coastaldelight@example.com', '+91 8324567194', '88, Coastal Delight Street, Kolkata', 'Kolkata', 'West Bengal', '110031', 'Rice and Fish curry', '00:00:16', '00:00:20'),
(45, 'Rajput Spice', 'rajputspice@example.com', '+91 8065237914', '42, Rajput Spice Street, Jaipur', 'Jaipur', 'Rajasthan', '110088', 'Indian Cuisine', '00:00:10', '00:00:14'),
(46, 'Mumbai Flavors', 'mumbaiflavors@example.com', '+91 8991246357', '34, Mumbai Flavors Street, Mumbai', 'Mumbai', 'Maharashtra', '110066', 'Indian Cuisine', '00:00:13', '00:00:18'),
(47, 'Golden Masala', 'goldenmasala@example.com', '+91 8264593721', '18, Golden Masala Street, Chennai', 'Chennai', 'Tamil Nadu', '110069', 'Biryani', '00:00:12', '00:00:15'),
(48, 'Delhi Darbar', 'delhidarbar@example.com', '+91 8932456781', '54, Delhi Darbar Street, Delhi', 'Delhi', 'New Delhi', '110048', 'Indian Cuisine', '00:00:09', '00:00:13'),
(49, 'Flavor Street', 'flavorstreet@example.com', '+91 8051246739', '99, Flavor Street Street, Pune', 'Pune', 'Maharashtra', '110010', 'Indian Cuisine', '00:00:14', '00:00:17'),
(50, 'Biryani Crave', 'biryanicrave@example.com', '+91 8231456072', '71, Biryani Crave Street, Hyderabad', 'Hyderabad', 'Andhra Pradesh', '110093', 'Biryani', '00:00:14', '00:00:20');