--
-- Table structure for table subscriptions
--
CREATE TABLE `prefix_subscriptions` (
  `username` varchar(75) NOT NULL default '',
  `firstname` varchar(75) NOT NULL default '',
  `lastname` varchar(75) NOT NULL default '',
  `mail` varchar(75) NOT NULL default '',
  `password` varchar(75) NOT NULL default '',
  PRIMARY KEY  (`username`)
) ENGINE=MYISAM CHARACTER SET utf8 COLLATE utf8_unicode_ci;
