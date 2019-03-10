-- MySQL dump 10.13  Distrib 5.7.25, for Linux (x86_64)
--
-- Host: localhost    Database: hrbot
-- ------------------------------------------------------
-- Server version	5.7.25-0ubuntu0.18.04.2

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Profile`
--

DROP TABLE IF EXISTS `Profile`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Profile` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `resume_path` text NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Profile`
--

LOCK TABLES `Profile` WRITE;
/*!40000 ALTER TABLE `Profile` DISABLE KEYS */;
INSERT INTO `Profile` VALUES (1,'jijijii','uhuhu@huhu.com','nnmnmnmn','/home/user/codiecon/hrbot/pdf/1.pdf'),(2,'Shripad','shripad@coolboy.com','asdfghjkl','/home/user/codiecon/hrbot/pdf/2.pdf');
/*!40000 ALTER TABLE `Profile` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Questions`
--

DROP TABLE IF EXISTS `Questions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Questions` (
  `id` int(11) DEFAULT NULL,
  `question` varchar(255) DEFAULT NULL,
  `category` varchar(255) DEFAULT NULL,
  `answer` text
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Questions`
--

LOCK TABLES `Questions` WRITE;
/*!40000 ALTER TABLE `Questions` DISABLE KEYS */;
INSERT INTO `Questions` VALUES (1,'What is this keyword in JavaScript?','javascript','This keyword refers to the object from where it was called.The JavaScript this keyword refers to the object it belongs to. This points to a particular object.'),(2,'What is === operator?','javascript',' === is called as strict equality operator which returns true when the two operands are having the same value without any type conversion.An operator which perform strict equality comparisons.'),(3,'What is JavaScript?','javascript',' JavaScript is a client-side as well as server side scripting language that can be inserted into HTML pages and is understood by web browsers. JavaScript is also an Object based Programming language'),(4,'What is the difference between ViewState and SessionState?','javascript',' ViewState is specific to a page in a session.Session State is specific to user specific data that can be accessed across all pages in the web application.'),(5,'What is the use of isNaN function?','javascript',' isNan function returns true if the argument is not a number otherwise it is false.'),(6,'What is dictionary in Python?','python',' The built-in datatypes in Python is called dictionary. It defines one-to-one relationship between keys and values. Dictionaries contain pair of keys and their corresponding values. Dictionaries are indexed by keys.'),(7,' How is Multithreading achieved in Python?','python','Python has a multi-threading package but if you want to multi-thread to speed your code up'),(8,'Explain Inheritance in Python with an example.','python','Inheritance allows One class to gain all the members(say attributes and methods) of another class. Inheritance provides code reusability makes it easier to create and maintain an application. The class from which we are inheriting is called super-class and the class that is inherited is called a derived / child class.They are different types of inheritance supported by Python: Single Inheritance â€“ where a derived class acquires the members of a single super class. Multi-level inheritance â€“ a derived class d1 in inherited from base class base1 and d2 are inherited from base2. Hierarchical inheritance â€“ from one base class you can inherit any number of child classes. Multiple inheritance â€“ a derived class is inherited from more than one base class'),(9,'Whenever Python exits why isnt all the memory de-allocated?','python',' Whenever Python exits especially those Python modules which are having circular references to other objects or the objects that are referenced from the global namespaces are not always de-allocated or freed. It is impossible to de-allocate those portions of memory that are reserved by the C library. On exit because of having its own efficient clean up mechanism Python would try to de-allocate/destroy every other object.'),(10,'Explain what Flask is and its benefits?','python',' Flask is a web microframework for Python based on Werkzeug Jinja2 and good intentions BSD license. Werkzeug and Jinja2 are two of its dependencies. This means it will have little to no dependencies on external libraries.  It makes the framework light while there is a little dependency to update and fewer security bugs.'),(11,'In how many ways can a CSS be integrated as a web page?','css',' CSS can be integrated in three ways :  inline internal and external.'),(12,'What are Pseudo-elements?','css',' Pseudo-elements are keyword added to the selector that allows one o style a specific part of the selected element. CSS in used to apply styles in HTML mark-up. In some cases when extra mark-up or styling is not possible for the document then there is a feature available in CSS known as pseudo-elements. It will allow extra mark-up to the document without disturbing the actual document. It can be used for;To style the first letter line or element.To insert a content.'),(13,'What is the purpose of the z-index and how is it used?','css',' The z-index helps specify the stack order of positioned elements that may overlap one another. The z-index default value is zero and can take on either a positive or negative number. An element with a higher z-index is always stacked above than a lower index. Z-Index can take the following values: Auto: Sets the stack order equal to its parents. Number: Orders the stack order. Initial: Sets this property to its default value (0). Inherit: Inherits this property from its parent element.'),(14,'What is CSS Box Model and what are its elements?','css',' The CSS box defines the design and the layout of elements of CSS. The several elements are: Margin: transparent area outside border. Border: the padding and content option with a border around it is shown. Padding: Space is around content. Padding is transparent. Content: box where text and images appear.'),(15,'What is a CSS selector?','css',' It is a string that identifies the elements to which a particular declaration apply. It is also referred as a link between the HTML document and the style sheet. It is equivalent of HTML elements.'),(16,'What are the types of layout available in Bootstrap?','bootstrap','In Bootstrap there are two types of Layout available. Fluid Layout: Fluid layout is used when you want to create a app that is 100% wide and use up all the width of the screen. Fixed Layout: For a standard screen you will use fixed layout (940 px) option'),(17,'What is the use of Jumbotron in Bootstrap?','bootstrap','In bootstrap - Jumbotron is generally used for content that you want to highlight like some slogan or marketing headline etc. in other words it is used to enlarge the size of the headings and to add a margin for landing page content To use the Jumbotron in Bootstrap Create a container< div> with the class of .jumbotron'),(18,'In Bootstrap what are the two ways you can display the code?','bootstrap','< code> tag : If you are going to display code inline'),(19,'What does Bootstrap package includes?','bootstrap','Bootstrap package includes â€“ Scaffolding â€“ Bootstrap provides a basic structure with Grid System link styles'),(20,'What are global styles that are used in Bootstrap Default Typography?','bootstrap','In Bootstrap the global default font-size is 14px and the line height is 1.428. The default font changes to Helvetica and Arial are with sans-serif fallback and all these styles are applicable for both body and all paragraphs.'),(21,'What are web workers?','html','A web worker is a script that runs in the background ( in another thread) without the page needing to wait for it to complete. The user can continue to interact with the page while the web worker runs in the background. Workers utilize thread-like message passing to achieve parallelism.'),(22,'Briefly describe the correct usage of the following HTML5 semantic elements: <header>; <article>; <section>; <footer>;','HTML','The <header> element is used to contain introductory and navigational information about a section of the page. This can include the section heading the authors name time and date of publication table of contents or other navigational information. The <article> element is meant to house a self-contained composition that can logically be independently recreated outside of the page without losing itâ€™s meaining. Individual blog posts or news stories are good examples. The <section> element is a flexible container for holding content that shares a common informational theme or purpose. The <footer> element is used to hold information that should appear at the end of a section of content and contain additional information about the section. Authors name copyright information and related links are typical examples of such content.'),(23,'What is HTML5 Web Storage? Explain localStorage and sessionStorage.','html','With HTML5 web pages can store data locally within the users browser. Earlier this was done with cookies. However Web Storage is more secure and faster. The data is not included with every server request but used ONLY when asked for. The data is stored in name/value pairs and a web page can only access data stored by itself. Unlike cookies the storage limit is far larger (at least 5MB) and information is never transferred to the server. The difference between localStorage and sessionStorage involves the lifetime and scope of the storage. Data stored through localStorage is permanent: it does not expire and remains stored on the userâ€™s computer until a web app deletes it or the user asks the browser to delete it. SessionStorage has the same lifetime as the top-level window or browser tab in which the script that stored it is running. When the window or tab is permanently closed any data stored through sessionStorage is deleted. Both forms of storage are scoped to the document origin so that documents with different origins will never share the stored objects. But sessionStorage is also scoped on a per-window basis. If a user has two browser tabs displaying documents from the same origin those two tabs have separate sessionStorage data: the scripts running in one tab cannot read or overwrite the data written by scripts in the other tab even if both tabs are visiting exactly the same page and are running exactly the same scripts.'),(24,'What is the difference between span and div?','html','The difference is that span gives the output with display: inline and div gives the output with display: block. span is used when we need our elements to be shown in a line one after the other.'),(25,'Whatâ€™s the difference between the <svg> and <canvas> elements?','html','The <svg> element is a container for SVG graphics. SVG has several methods for drawing paths boxes circles text and even bitmap images. SVG is a language for describing 2D graphics but <canvas> allows you to draw 2D graphics on the fly using JavaScript. SVG is XML-based which means that every element is available within the SVG DOM. You can attach JavaScript event handlers for an element. In SVG each drawn shape is remembered as an object. If attributes of an SVG object are changed the browser can automatically re-render the shape. Canvas is rendered pixel by pixel. In canvas once the graphic is drawn it is forgotten by the browser. If its position should be changed the entire scene needs to be redrawn including any objects that might have been covered by the graphic.'),(26,'What is Callback in node.js?','nodejs','Callback function is used in node.js to deal with multiple requests made to the server. Like if you have a large file which is going to take a long time for a server to read and if you dont want a server to get engage in reading that large file while dealing with other requests call back function is used. Call back function allows the server to deal with pending request first and call a function when it is finished.'),(27,'What is the difference between process.nextTick() and setImmediate() ?','nodejs','The difference between process.nextTick() and setImmediate() is that process.nextTick() defers the execution of an action till the next pass around the event loop or it simply calls the callback function once the ongoing execution of the event loop is finished whereas setImmediate() executes a callback on the next cycle of the event loop and it gives back to the event loop for executing any I/O operations.'),(28,'What Is Package.Json? Who Uses It?','nodejs','It is a plain JSON (JavaScript Object Notation) text file which contains all metadata information about Node.js Project or application. This file should be present in the root directory of every Node.js Package or Module to describe its metadata in JSON format. The file is named as â€œpackageâ€ because Node.js platform treats every feature as a separate component. Node.js calls these as Package or Module. NPM (Node Package Manager) uses <package.json> file. It includes details of the Node.js application or package. This file contains a no. of different directives or elements. These directives guide NPM about how to handle a module or package.'),(29,'What is callback hell and how can it be avoided?','nodejs','Callback hell is when you have a lot of callbacks inside callbacks. Which keeps indenting the code to the right to a point where it is no longer readable and nor maintainable. There are two ways to avoid it. By the use of a promgramming construct called Promises. Using promises you could still write callbacks but now they were chainable. So instead of code indenting to right. It now increased in vertical direction. Which solved the major problem of callback hell but still the code was verbose and lot of thens had to be written which made it a little less pleasing. Using the new async/await. Async await removes the .then blocks of your code and replace them with try and catch blocks which are usually the traits of a synchronous design pattern.'),(30,'If Node is single threaded then how it handles concurrency','nodejs','Node provides a single thread to programmers so that code can be written easily and without bottleneck. Node internally uses multiple POSIX threads for various I/O operations such as File DNS Network calls etc.When Node gets I/O request it creates or uses a thread to perform that I/O operation and once the operation is done it pushes the result to the event queue. On each such event event loop runs and checks the queue and if the execution stack of Node is empty then it adds the queue result to execution stack. This is how Node manages concurrency. '),(31,'What is PHP?','php','PHP is a web language based on scripts that allow developers to dynamically create generated web pages.'),(32,'What is the meaning of a final class and a final method?','php','final is introduced in PHP5. Final class means that this class cannot be extended and a final method cannot be overridden.'),(33,'How can we display information of a variable and readable by a human with PHP?','php','To be able to display a human-readable result we use print_r().'),(34,'How be the result set of Mysql handled in PHP?','php','The result set can be handled using mysqli_fetch_array  mysqli_fetch_assoc mysqli_fetch_object or mysqli_fetch_row.'),(35,'Which cryptographic extension provide generation and verification of digital signatures?','php','The PHP-OpenSSL extension provides several cryptographic operations including generation and verification of digital signatures.'),(36,'What is SQL Server?','mysql','SQL Server is   one of the Database Management Systems (DBMS) and is designed by Microsoft.  DBMS are computer software applications with the capability of interacting with user various other applications as well as the database itself. The objective is capturing and analyzing data and manages definition querying creation updating as well as administration of database.'),(37,'What are meant by Joins in MySQL?','mysql','In MySQL the Joins are used to query data from two or more tables. The query is made using relationship between certain columns existing in the table. There are four types of Joins in MySQL. Inner Join returns the rows if there is at least one match in both the tables. Left Join returns all the rows form the left table even if there is no match in the right table. Right Join returns all the rows from the right table even if no matches exist in left table. Full Join would return rows when there is at least one match in the tables.'),(38,'What is the difference between CHAR and VARCHAR?','mysql','When the table is created CHAR is used to define the fixed length of the table and columns. The length value could be in the range of 1-255. VARCHAR command is given to adjust the column and table length as required.'),(39,'What are the different types of strings in Database columns in MySQL?','mysql','Different types of strings that can be used for database columns are SET BLOB VARCHAR TEXT ENUM and CHAR.'),(40,'Is there an object oriented version of MySQL library functions?','mysql','MySQLi is the object oriented version of MySQL and it interfaces in PHP.');
/*!40000 ALTER TABLE `Questions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `SubmittedQuestions`
--

DROP TABLE IF EXISTS `SubmittedQuestions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `SubmittedQuestions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `profile_id` int(11) NOT NULL,
  `question` varchar(255) DEFAULT NULL,
  `answer` text,
  `score` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `SubmittedQuestions`
--

LOCK TABLES `SubmittedQuestions` WRITE;
/*!40000 ALTER TABLE `SubmittedQuestions` DISABLE KEYS */;
/*!40000 ALTER TABLE `SubmittedQuestions` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-03-10  6:25:39
