-- phpMyAdmin SQL Dump
-- version 4.6.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 22, 2019 at 08:07 AM
-- Server version: 5.7.14
-- PHP Version: 5.6.25

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `aira`
--

-- --------------------------------------------------------

--
-- Table structure for table `airapanel_billing`
--

CREATE TABLE `airapanel_billing` (
  `id` int(11) NOT NULL,
  `payer` varchar(10) COLLATE utf16_unicode_ci NOT NULL,
  `payee` varchar(10) COLLATE utf16_unicode_ci NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf16 COLLATE=utf16_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `airapanel_billing_items`
--

CREATE TABLE `airapanel_billing_items` (
  `id` int(11) NOT NULL,
  `billing_id` int(11) NOT NULL,
  `itemsbilling_id` int(11) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf16 COLLATE=utf16_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `airapanel_categories`
--

CREATE TABLE `airapanel_categories` (
  `id` int(11) NOT NULL,
  `name` varchar(120) COLLATE utf16_unicode_ci NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf16 COLLATE=utf16_unicode_ci;

--
-- Dumping data for table `airapanel_categories`
--

INSERT INTO `airapanel_categories` (`id`, `name`) VALUES
(1, 'technology'),
(2, 'electronics'),
(3, 'kitchen'),
(4, 'office'),
(5, 'developement');

-- --------------------------------------------------------

--
-- Table structure for table `airapanel_companies`
--

CREATE TABLE `airapanel_companies` (
  `id` int(11) NOT NULL,
  `name` varchar(120) COLLATE utf16_unicode_ci NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf16 COLLATE=utf16_unicode_ci;

--
-- Dumping data for table `airapanel_companies`
--

INSERT INTO `airapanel_companies` (`id`, `name`) VALUES
(9, 'google'),
(8, 'wipro'),
(7, 'tcs'),
(6, 'codedady'),
(10, 'apple'),
(11, 'facebook');

-- --------------------------------------------------------

--
-- Table structure for table `airapanel_customers`
--

CREATE TABLE `airapanel_customers` (
  `id` int(11) NOT NULL,
  `name` varchar(120) COLLATE utf16_unicode_ci NOT NULL,
  `aira_code` varchar(120) COLLATE utf16_unicode_ci DEFAULT NULL,
  `address` varchar(120) COLLATE utf16_unicode_ci DEFAULT NULL,
  `country` varchar(120) COLLATE utf16_unicode_ci DEFAULT NULL,
  `state` varchar(120) COLLATE utf16_unicode_ci DEFAULT NULL,
  `city_one` varchar(120) COLLATE utf16_unicode_ci DEFAULT NULL,
  `city_two` varchar(120) COLLATE utf16_unicode_ci DEFAULT NULL,
  `phone` varchar(20) COLLATE utf16_unicode_ci DEFAULT NULL,
  `mobile` varchar(20) COLLATE utf16_unicode_ci DEFAULT NULL,
  `job_position` varchar(100) COLLATE utf16_unicode_ci DEFAULT NULL,
  `email` varchar(254) COLLATE utf16_unicode_ci DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf16 COLLATE=utf16_unicode_ci;

--
-- Dumping data for table `airapanel_customers`
--

INSERT INTO `airapanel_customers` (`id`, `name`, `aira_code`, `address`, `country`, `state`, `city_one`, `city_two`, `phone`, `mobile`, `job_position`, `email`) VALUES
(6, 'zuckerberg', 'CUST6', '', '', '', '', '', '', '', '', ''),
(5, 'sundar pichai', 'CUST1', '', '', '', '', '', '', '', '', ''),
(7, 'Satya Nadella', 'CUST7', '', '', '', '', '', '', '', '', ''),
(8, 'Eduardo Cue', 'CUST8', '', '', '', '', '', '', '', '', ''),
(9, 'Tim Cook', 'CUST9', '', '', '', '', '', '', '', '', '');

-- --------------------------------------------------------

--
-- Table structure for table `airapanel_history`
--

CREATE TABLE `airapanel_history` (
  `id` int(11) NOT NULL,
  `sales_id` varchar(20) COLLATE utf16_unicode_ci DEFAULT NULL,
  `invoice_id` varchar(20) COLLATE utf16_unicode_ci DEFAULT NULL,
  `type` varchar(20) COLLATE utf16_unicode_ci NOT NULL,
  `created_at` datetime(6) NOT NULL,
  `modified_at` datetime(6) DEFAULT NULL,
  `description` varchar(255) COLLATE utf16_unicode_ci DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf16 COLLATE=utf16_unicode_ci;

--
-- Dumping data for table `airapanel_history`
--

INSERT INTO `airapanel_history` (`id`, `sales_id`, `invoice_id`, `type`, `created_at`, `modified_at`, `description`) VALUES
(1, '11', NULL, 'quotation', '2019-12-04 07:05:30.025727', '2019-12-04 12:35:30.021769', 'quotation confirmed'),
(2, '12', NULL, 'quotation', '2019-12-04 07:07:21.411571', '2019-12-04 12:37:21.407615', 'quotation confirmed'),
(3, '13', NULL, 'quotation', '2019-12-04 09:17:27.100295', '2019-12-04 14:47:27.096307', 'quotation confirmed'),
(4, '14', NULL, 'quotation', '2019-12-04 09:33:14.286647', '2019-12-04 15:03:14.283643', 'quotation confirmed'),
(5, '15', NULL, 'quotation', '2019-12-04 09:33:18.151946', '2019-12-04 15:03:18.149951', 'quotation confirmed'),
(6, '16', NULL, 'quotation', '2019-12-04 09:33:19.219551', '2019-12-04 15:03:19.217540', 'quotation confirmed'),
(7, '17', NULL, 'quotation', '2019-12-04 09:33:20.158273', '2019-12-04 15:03:20.156278', 'quotation confirmed'),
(8, '18', NULL, 'quotation', '2019-12-04 09:34:11.498638', '2019-12-04 15:04:11.495645', 'quotation confirmed'),
(9, '19', NULL, 'quotation', '2019-12-04 09:34:16.019275', '2019-12-04 15:04:16.017279', 'quotation confirmed'),
(10, '20', NULL, 'quotation', '2019-12-04 09:34:19.006423', '2019-12-04 15:04:19.005426', 'quotation confirmed'),
(11, '21', NULL, 'quotation', '2019-12-04 09:34:21.113957', '2019-12-04 15:04:21.112946', 'quotation confirmed'),
(12, '22', NULL, 'quotation', '2019-12-04 09:34:22.198169', '2019-12-04 15:04:22.196174', 'quotation confirmed'),
(13, '23', NULL, 'quotation', '2019-12-04 09:34:22.994889', '2019-12-04 15:04:22.993892', 'quotation confirmed'),
(14, '24', NULL, 'quotation', '2019-12-04 09:35:11.884048', '2019-12-04 15:05:11.881058', 'quotation confirmed'),
(15, '25', NULL, 'quotation', '2019-12-04 09:35:13.065896', '2019-12-04 15:05:13.063901', 'quotation confirmed'),
(16, '26', NULL, 'quotation', '2019-12-04 09:35:13.886431', '2019-12-04 15:05:13.884467', 'quotation confirmed'),
(17, '27', NULL, 'quotation', '2019-12-04 09:35:14.686297', '2019-12-04 15:05:14.684330', 'quotation confirmed'),
(18, '28', NULL, 'quotation', '2019-12-04 09:35:15.418819', '2019-12-04 15:05:15.417821', 'quotation confirmed'),
(19, '29', NULL, 'quotation', '2019-12-04 09:35:16.168814', '2019-12-04 15:05:16.167816', 'quotation confirmed'),
(20, '30', NULL, 'quotation', '2019-12-04 09:35:16.938739', '2019-12-04 15:05:16.937759', 'quotation confirmed'),
(21, '31', NULL, 'quotation', '2019-12-04 09:35:17.999653', '2019-12-04 15:05:17.998689', 'quotation confirmed'),
(22, '32', NULL, 'quotation', '2019-12-04 09:35:18.856101', '2019-12-04 15:05:18.854105', 'quotation confirmed'),
(23, '33', NULL, 'quotation', '2019-12-04 09:35:43.243590', '2019-12-04 15:05:43.241621', 'quotation confirmed'),
(24, '34', NULL, 'quotation', '2019-12-04 09:35:44.027483', '2019-12-04 15:05:44.025488', 'quotation confirmed'),
(25, '35', NULL, 'quotation', '2019-12-04 09:35:44.717161', '2019-12-04 15:05:44.715166', 'quotation confirmed'),
(26, '36', NULL, 'quotation', '2019-12-04 09:35:45.321392', '2019-12-04 15:05:45.320393', 'quotation confirmed'),
(27, '37', NULL, 'quotation', '2019-12-04 09:35:46.164247', '2019-12-04 15:05:46.163249', 'quotation confirmed'),
(28, '38', NULL, 'quotation', '2019-12-04 09:35:46.825197', '2019-12-04 15:05:46.824201', 'quotation confirmed'),
(29, '39', NULL, 'quotation', '2019-12-04 09:35:47.626157', '2019-12-04 15:05:47.624194', 'quotation confirmed'),
(30, '40', NULL, 'quotation', '2019-12-04 09:35:48.094901', '2019-12-04 15:05:48.093905', 'quotation confirmed'),
(31, '41', NULL, 'quotation', '2019-12-04 09:35:48.738851', '2019-12-04 15:05:48.736857', 'quotation confirmed'),
(32, '42', NULL, 'quotation', '2019-12-04 09:35:49.334277', '2019-12-04 15:05:49.331270', 'quotation confirmed'),
(33, '43', NULL, 'quotation', '2019-12-04 09:35:49.943340', '2019-12-04 15:05:49.942345', 'quotation confirmed'),
(34, '44', NULL, 'quotation', '2019-12-04 09:35:50.554707', '2019-12-04 15:05:50.553714', 'quotation confirmed'),
(35, '45', NULL, 'quotation', '2019-12-04 09:35:51.182419', '2019-12-04 15:05:51.180426', 'quotation confirmed'),
(36, '46', NULL, 'quotation', '2019-12-04 09:35:51.686441', '2019-12-04 15:05:51.684449', 'quotation confirmed'),
(37, '47', NULL, 'quotation', '2019-12-04 09:35:52.313736', '2019-12-04 15:05:52.312735', 'quotation confirmed'),
(38, '48', NULL, 'quotation', '2019-12-04 09:35:52.905772', '2019-12-04 15:05:52.904776', 'quotation confirmed'),
(39, '49', NULL, 'quotation', '2019-12-04 09:35:53.517718', '2019-12-04 15:05:53.516725', 'quotation confirmed'),
(40, '50', NULL, 'quotation', '2019-12-04 09:35:54.197448', '2019-12-04 15:05:54.196484', 'quotation confirmed'),
(41, '51', NULL, 'quotation', '2019-12-04 09:35:54.690787', '2019-12-04 15:05:54.689777', 'quotation confirmed'),
(42, '52', NULL, 'quotation', '2019-12-04 09:35:55.271623', '2019-12-04 15:05:55.269629', 'quotation confirmed'),
(43, '53', NULL, 'quotation', '2019-12-04 09:35:55.798566', '2019-12-04 15:05:55.796569', 'quotation confirmed'),
(44, '54', NULL, 'quotation', '2019-12-05 07:31:55.687678', '2019-12-05 13:01:55.545059', 'quotation confirmed'),
(45, '55', NULL, 'quotation', '2019-12-05 07:31:59.056212', '2019-12-05 13:01:59.054254', 'quotation confirmed'),
(46, '56', NULL, 'quotation', '2019-12-05 07:32:00.808367', '2019-12-05 13:02:00.806371', 'quotation confirmed'),
(47, '57', NULL, 'quotation', '2019-12-05 07:32:02.019837', '2019-12-05 13:02:02.017840', 'quotation confirmed'),
(48, '58', NULL, 'quotation', '2019-12-05 07:32:03.028989', '2019-12-05 13:02:03.027992', 'quotation confirmed'),
(49, '59', NULL, 'quotation', '2019-12-05 07:32:04.093807', '2019-12-05 13:02:04.091833', 'quotation confirmed'),
(50, '60', NULL, 'quotation', '2019-12-05 07:32:05.237759', '2019-12-05 13:02:05.236725', 'quotation confirmed'),
(51, '61', NULL, 'quotation', '2019-12-05 07:32:06.194770', '2019-12-05 13:02:06.192776', 'quotation confirmed'),
(52, '62', NULL, 'quotation', '2019-12-05 07:32:07.085875', '2019-12-05 13:02:07.083882', 'quotation confirmed'),
(53, '63', NULL, 'quotation', '2019-12-05 07:32:09.774114', '2019-12-05 13:02:09.773116', 'quotation confirmed'),
(54, '64', NULL, 'quotation', '2019-12-05 07:33:11.221264', '2019-12-05 13:03:11.219270', 'quotation confirmed'),
(55, '65', NULL, 'quotation', '2019-12-05 10:34:11.025780', '2019-12-05 16:04:11.022788', 'quotation confirmed'),
(56, '65', NULL, 'saleorder', '2019-12-05 10:34:34.946565', '2019-12-05 16:04:34.929610', 'Nothing to invoice'),
(57, '65', NULL, 'saleorder', '2019-12-05 10:39:12.970808', '2019-12-05 16:09:12.966854', 'Nothing to invoice'),
(58, '65', NULL, 'quotation', '2019-12-05 11:12:57.675893', '2019-12-05 16:42:57.670902', 'quotation cancelled'),
(59, '65', NULL, 'invoice', '2019-12-05 11:15:16.244424', '2019-12-05 16:45:16.241427', 'saleorder to invoice'),
(60, '65', '15', 'invoice', '2019-12-05 12:03:22.671881', '2019-12-05 17:33:22.651934', 'saleorder to invoice'),
(61, '65', '16', 'invoice', '2019-12-05 12:06:29.729272', '2019-12-05 17:36:29.710321', 'saleorder to invoice'),
(62, '63', '17', 'invoice', '2019-12-05 12:25:19.794560', '2019-12-05 17:55:19.756662', 'saleorder to invoice'),
(63, '63', '18', 'invoice', '2019-12-05 12:25:36.828388', '2019-12-05 17:55:36.796473', 'saleorder to invoice'),
(64, '63', '19', 'invoice', '2019-12-05 12:25:38.949104', '2019-12-05 17:55:38.915194', 'saleorder to invoice'),
(65, '63', '20', 'invoice', '2019-12-05 12:25:39.811423', '2019-12-05 17:55:39.780512', 'saleorder to invoice'),
(66, '63', '21', 'invoice', '2019-12-05 12:25:55.860351', '2019-12-05 17:55:55.835417', 'saleorder to invoice'),
(67, NULL, '22', 'invoice', '2019-12-07 07:32:48.245521', '2019-12-07 13:02:48.243526', 'invoice saved'),
(68, NULL, '23', 'invoice', '2019-12-07 07:37:45.044815', '2019-12-07 13:07:45.033845', 'invoice saved'),
(69, NULL, '24', 'invoice', '2019-12-07 07:37:56.503497', '2019-12-07 13:07:56.501500', 'invoice saved'),
(70, NULL, '25', 'invoice', '2019-12-07 07:51:12.635077', '2019-12-07 13:21:12.633082', 'invoice saved'),
(73, NULL, '28', 'invoice', '2019-12-07 08:08:14.566691', '2019-12-07 13:38:14.557717', 'invoice saved'),
(74, NULL, '29', 'invoice', '2019-12-07 08:08:23.896379', '2019-12-07 13:38:23.895381', 'invoice posted'),
(75, NULL, '30', 'invoice', '2019-12-07 08:11:35.905259', '2019-12-07 13:41:35.902267', 'invoice posted'),
(76, NULL, '31', 'invoice', '2019-12-07 10:25:22.388575', '2019-12-07 15:55:22.382657', 'invoice posted'),
(77, NULL, '32', 'invoice', '2019-12-07 10:26:20.183700', '2019-12-07 15:56:20.181425', 'invoice posted'),
(78, NULL, '33', 'invoice', '2019-12-07 10:26:21.529009', '2019-12-07 15:56:21.516222', 'invoice posted'),
(79, NULL, '34', 'invoice', '2019-12-07 10:26:22.511636', '2019-12-07 15:56:22.498150', 'invoice posted'),
(80, NULL, '35', 'invoice', '2019-12-07 10:26:23.361980', '2019-12-07 15:56:23.350774', 'invoice posted'),
(81, NULL, '36', 'invoice', '2019-12-07 10:26:24.244535', '2019-12-07 15:56:24.228581', 'invoice posted'),
(82, NULL, '37', 'invoice', '2019-12-07 10:26:25.119754', '2019-12-07 15:56:25.104768', 'invoice posted'),
(83, NULL, '38', 'invoice', '2019-12-07 10:26:26.208341', '2019-12-07 15:56:26.195331', 'invoice posted'),
(84, NULL, '39', 'invoice', '2019-12-19 07:28:21.219812', '2019-12-19 12:58:21.162960', 'invoice posted'),
(85, NULL, '40', 'invoice', '2019-12-19 07:29:43.409282', '2019-12-19 12:59:43.405291', 'invoice posted');

-- --------------------------------------------------------

--
-- Table structure for table `airapanel_invoices`
--

CREATE TABLE `airapanel_invoices` (
  `id` int(11) NOT NULL,
  `customer_id` int(11) DEFAULT NULL,
  `company_id` int(11) DEFAULT NULL,
  `created` datetime(6) NOT NULL,
  `due_date` datetime(6) NOT NULL,
  `total_amount` varchar(12) COLLATE utf16_unicode_ci DEFAULT NULL,
  `paid_amount` varchar(12) COLLATE utf16_unicode_ci DEFAULT NULL,
  `status` varchar(20) COLLATE utf16_unicode_ci DEFAULT NULL,
  `type` varchar(20) COLLATE utf16_unicode_ci NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf16 COLLATE=utf16_unicode_ci;

--
-- Dumping data for table `airapanel_invoices`
--

INSERT INTO `airapanel_invoices` (`id`, `customer_id`, `company_id`, `created`, `due_date`, `total_amount`, `paid_amount`, `status`, `type`) VALUES
(15, 6, 11, '2019-12-05 12:03:22.655931', '2019-03-28 00:00:00.000000', '25000', NULL, NULL, 'invoice'),
(16, 6, 11, '2019-12-05 12:06:29.715309', '2019-03-28 00:00:00.000000', '25000', NULL, NULL, 'invoice'),
(17, 6, 11, '2019-12-05 12:25:19.761649', '2019-03-28 00:00:00.000000', '25000', NULL, NULL, 'invoice'),
(18, 6, 11, '2019-12-05 12:25:36.801474', '2019-03-28 00:00:00.000000', '25000', NULL, NULL, 'invoice'),
(19, 6, 11, '2019-12-05 12:25:38.921179', '2019-03-28 00:00:00.000000', '25000', NULL, NULL, 'invoice'),
(20, 6, 11, '2019-12-05 12:25:39.784494', '2019-03-28 00:00:00.000000', '25000', NULL, NULL, 'invoice'),
(21, 6, 11, '2019-12-05 12:25:55.840404', '2019-03-28 00:00:00.000000', '25000', NULL, NULL, 'invoice'),
(28, NULL, NULL, '2019-12-07 08:08:14.557717', '2019-02-25 00:00:00.000000', '25000', '1023.2', 'draft', 'invoice'),
(29, NULL, NULL, '2019-12-07 08:08:23.895381', '2019-02-25 00:00:00.000000', '25000', '25023.2', 'paid', 'invoice'),
(30, NULL, NULL, '2019-12-07 08:11:35.902267', '2019-02-25 00:00:00.000000', '25000', '2523.2', 'paritally_paid', 'invoice'),
(31, NULL, NULL, '2019-12-07 10:25:22.383633', '2019-02-25 00:00:00.000000', '25000', '1023.2', 'posted', 'fastbill'),
(32, NULL, NULL, '2019-12-07 10:26:20.181425', '2019-02-25 00:00:00.000000', '25000', '1023.2', 'posted', 'fastbill'),
(33, NULL, NULL, '2019-12-07 10:26:21.516222', '2019-02-25 00:00:00.000000', '25000', '1023.2', 'posted', 'fastbill'),
(34, NULL, NULL, '2019-12-07 10:26:22.498627', '2019-02-25 00:00:00.000000', '25000', '1023.2', 'posted', 'fastbill'),
(35, NULL, NULL, '2019-12-07 10:26:23.350774', '2019-02-25 00:00:00.000000', '25000', '1023.2', 'posted', 'fastbill'),
(36, NULL, NULL, '2019-12-07 10:26:24.229136', '2019-02-25 00:00:00.000000', '25000', '1023.2', 'posted', 'fastbill'),
(37, NULL, NULL, '2019-12-07 10:26:25.105857', '2019-02-25 00:00:00.000000', '25000', '1023.2', 'posted', 'fastbill'),
(38, NULL, NULL, '2019-12-07 10:26:26.195801', '2019-02-25 00:00:00.000000', '25000', '1023.2', 'posted', 'fastbill'),
(39, NULL, NULL, '2019-12-19 07:28:21.163958', '2019-02-25 00:00:00.000000', '50000', '5000.0', 'posted', 'fastbill'),
(40, NULL, NULL, '2019-12-19 07:29:43.406288', '2019-02-25 00:00:00.000000', '30000', '3000.0', 'posted', 'fastbill');

-- --------------------------------------------------------

--
-- Table structure for table `airapanel_invoices_history`
--

CREATE TABLE `airapanel_invoices_history` (
  `id` int(11) NOT NULL,
  `invoices_id` int(11) NOT NULL,
  `history_id` int(11) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf16 COLLATE=utf16_unicode_ci;

--
-- Dumping data for table `airapanel_invoices_history`
--

INSERT INTO `airapanel_invoices_history` (`id`, `invoices_id`, `history_id`) VALUES
(7, 28, 73),
(8, 29, 74),
(9, 30, 75),
(10, 31, 76),
(11, 32, 77),
(12, 33, 78),
(13, 34, 79),
(14, 35, 80),
(15, 36, 81),
(16, 37, 82),
(17, 38, 83),
(18, 39, 84),
(19, 40, 85);

-- --------------------------------------------------------

--
-- Table structure for table `airapanel_invoices_items`
--

CREATE TABLE `airapanel_invoices_items` (
  `id` int(11) NOT NULL,
  `invoices_id` int(11) NOT NULL,
  `items_relation_id` int(11) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf16 COLLATE=utf16_unicode_ci;

--
-- Dumping data for table `airapanel_invoices_items`
--

INSERT INTO `airapanel_invoices_items` (`id`, `invoices_id`, `items_relation_id`) VALUES
(101, 36, 100),
(100, 35, 99),
(99, 35, 98),
(98, 35, 97),
(97, 34, 96),
(96, 34, 95),
(95, 34, 94),
(94, 33, 93),
(93, 33, 92),
(92, 33, 91),
(91, 32, 90),
(90, 32, 89),
(89, 32, 88),
(88, 31, 87),
(87, 31, 86),
(86, 31, 85),
(85, 30, 84),
(84, 30, 83),
(83, 30, 82),
(82, 29, 81),
(81, 29, 80),
(80, 29, 79),
(79, 28, 78),
(78, 28, 77),
(77, 28, 76),
(76, 21, 183),
(75, 21, 182),
(74, 21, 181),
(73, 20, 183),
(72, 20, 182),
(71, 20, 181),
(70, 19, 183),
(69, 19, 182),
(68, 19, 181),
(67, 18, 183),
(66, 18, 182),
(65, 18, 181),
(64, 17, 183),
(63, 17, 182),
(62, 17, 181),
(102, 36, 101),
(103, 36, 102),
(104, 37, 103),
(105, 37, 104),
(106, 37, 105),
(107, 38, 106),
(108, 38, 107),
(109, 38, 108),
(110, 39, 109),
(111, 39, 110),
(112, 39, 111),
(113, 40, 112),
(114, 40, 113),
(115, 40, 114);

-- --------------------------------------------------------

--
-- Table structure for table `airapanel_invoices_payement_history`
--

CREATE TABLE `airapanel_invoices_payement_history` (
  `id` int(11) NOT NULL,
  `invoices_id` int(11) NOT NULL,
  `payemethistory_id` int(11) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf16 COLLATE=utf16_unicode_ci;

--
-- Dumping data for table `airapanel_invoices_payement_history`
--

INSERT INTO `airapanel_invoices_payement_history` (`id`, `invoices_id`, `payemethistory_id`) VALUES
(31, 29, 32),
(30, 29, 31),
(29, 29, 30),
(28, 30, 29),
(27, 30, 28),
(26, 30, 27),
(25, 29, 26),
(24, 28, 25),
(32, 40, 33);

-- --------------------------------------------------------

--
-- Table structure for table `airapanel_itemsbilling`
--

CREATE TABLE `airapanel_itemsbilling` (
  `id` int(11) NOT NULL,
  `billingid` varchar(20) COLLATE utf16_unicode_ci NOT NULL,
  `product_Id` varchar(20) COLLATE utf16_unicode_ci NOT NULL,
  `item_price` varchar(20) COLLATE utf16_unicode_ci NOT NULL,
  `tax` varchar(10) COLLATE utf16_unicode_ci NOT NULL,
  `amount` double NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf16 COLLATE=utf16_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `airapanel_itemsbilling_company`
--

CREATE TABLE `airapanel_itemsbilling_company` (
  `id` int(11) NOT NULL,
  `itemsbilling_id` int(11) NOT NULL,
  `companies_id` int(11) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf16 COLLATE=utf16_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `airapanel_itemsbilling_customer`
--

CREATE TABLE `airapanel_itemsbilling_customer` (
  `id` int(11) NOT NULL,
  `itemsbilling_id` int(11) NOT NULL,
  `customers_id` int(11) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf16 COLLATE=utf16_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `airapanel_items_relation`
--

CREATE TABLE `airapanel_items_relation` (
  `id` int(11) NOT NULL,
  `invoice_id` varchar(20) COLLATE utf16_unicode_ci DEFAULT NULL,
  `sales_id` varchar(20) COLLATE utf16_unicode_ci DEFAULT NULL,
  `item_price` varchar(20) COLLATE utf16_unicode_ci DEFAULT NULL,
  `tax` varchar(10) COLLATE utf16_unicode_ci DEFAULT NULL,
  `product_Id_id` int(11) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf16 COLLATE=utf16_unicode_ci;

--
-- Dumping data for table `airapanel_items_relation`
--

INSERT INTO `airapanel_items_relation` (`id`, `invoice_id`, `sales_id`, `item_price`, `tax`, `product_Id_id`) VALUES
(1, NULL, '3', '300', '12', 3),
(2, NULL, '3', '200', '5', 4),
(3, NULL, '3', '1000', '5', 6),
(4, NULL, '4', '300', '12', 3),
(5, NULL, '4', '200', '5', 4),
(6, NULL, '4', '1000', '5', 6),
(7, NULL, '5', '300', '12', 3),
(8, NULL, '5', '200', '5', 4),
(9, NULL, '5', '1000', '5', 6),
(10, NULL, '6', '300', '12', 3),
(11, NULL, '6', '200', '5', 4),
(12, NULL, '6', '1000', '5', 6),
(13, NULL, '7', '300', '12', 3),
(14, NULL, '7', '200', '5', 4),
(15, NULL, '7', '1000', '5', 6),
(16, NULL, '8', '300', '12', 3),
(17, NULL, '8', '200', '5', 4),
(18, NULL, '8', '1000', '5', 6),
(19, NULL, '9', '300', '12', 3),
(20, NULL, '9', '200', '5', 4),
(21, NULL, '9', '1000', '5', 6),
(22, NULL, '10', '300', '12', 3),
(23, NULL, '10', '200', '5', 4),
(24, NULL, '10', '1000', '5', 6),
(25, NULL, '11', '300', '12', 3),
(26, NULL, '11', '200', '5', 4),
(27, NULL, '11', '1000', '5', 6),
(28, NULL, '12', '300', '12', 3),
(29, NULL, '12', '200', '5', 4),
(30, NULL, '12', '1000', '5', 6),
(31, NULL, '13', '300', '12', 3),
(32, NULL, '13', '200', '5', 4),
(33, NULL, '13', '1000', '5', 6),
(34, NULL, '14', '300', '12', 3),
(35, NULL, '14', '200', '5', 4),
(36, NULL, '14', '1000', '5', 6),
(37, NULL, '15', '300', '12', 3),
(38, NULL, '15', '200', '5', 4),
(39, NULL, '15', '1000', '5', 6),
(40, NULL, '16', '300', '12', 3),
(41, NULL, '16', '200', '5', 4),
(42, NULL, '16', '1000', '5', 6),
(43, NULL, '17', '300', '12', 3),
(44, NULL, '17', '200', '5', 4),
(45, NULL, '17', '1000', '5', 6),
(46, NULL, '18', '300', '12', 3),
(47, NULL, '18', '200', '5', 4),
(48, NULL, '18', '1000', '5', 6),
(49, NULL, '19', '300', '12', 3),
(50, NULL, '19', '200', '5', 4),
(51, NULL, '19', '1000', '5', 6),
(52, NULL, '20', '300', '12', 3),
(53, NULL, '20', '200', '5', 4),
(54, NULL, '20', '1000', '5', 6),
(55, NULL, '21', '300', '12', 3),
(56, NULL, '21', '200', '5', 4),
(57, NULL, '21', '1000', '5', 6),
(58, NULL, '22', '300', '12', 3),
(59, NULL, '22', '200', '5', 4),
(60, NULL, '22', '1000', '5', 6),
(61, NULL, '23', '300', '12', 3),
(62, NULL, '23', '200', '5', 4),
(63, NULL, '23', '1000', '5', 6),
(64, NULL, '24', '300', '12', 3),
(65, NULL, '24', '200', '5', 4),
(66, NULL, '24', '1000', '5', 6),
(67, NULL, '25', '300', '12', 3),
(68, NULL, '25', '200', '5', 4),
(69, NULL, '25', '1000', '5', 6),
(70, NULL, '26', '300', '12', 3),
(71, NULL, '26', '200', '5', 4),
(72, NULL, '26', '1000', '5', 6),
(73, NULL, '27', '300', '12', 3),
(74, NULL, '27', '200', '5', 4),
(75, NULL, '27', '1000', '5', 6),
(76, NULL, '28', '300', '12', 3),
(77, NULL, '28', '200', '5', 4),
(78, NULL, '28', '1000', '5', 6),
(79, NULL, '29', '300', '12', 3),
(80, NULL, '29', '200', '5', 4),
(81, NULL, '29', '1000', '5', 6),
(82, NULL, '30', '300', '12', 3),
(83, NULL, '30', '200', '5', 4),
(84, NULL, '30', '1000', '5', 6),
(85, NULL, '31', '300', '12', 3),
(86, NULL, '31', '200', '5', 4),
(87, NULL, '31', '1000', '5', 6),
(88, NULL, '32', '300', '12', 3),
(89, NULL, '32', '200', '5', 4),
(90, NULL, '32', '1000', '5', 6),
(91, NULL, '33', '300', '12', 3),
(92, NULL, '33', '200', '5', 4),
(93, NULL, '33', '1000', '5', 6),
(94, NULL, '34', '300', '12', 3),
(95, NULL, '34', '200', '5', 4),
(96, NULL, '34', '1000', '5', 6),
(97, NULL, '35', '300', '12', 3),
(98, NULL, '35', '200', '5', 4),
(99, NULL, '35', '1000', '5', 6),
(100, NULL, '36', '300', '12', 3),
(101, NULL, '36', '200', '5', 4),
(102, NULL, '36', '1000', '5', 6),
(103, NULL, '37', '300', '12', 3),
(104, NULL, '37', '200', '5', 4),
(105, NULL, '37', '1000', '5', 6),
(106, NULL, '38', '300', '12', 3),
(107, NULL, '38', '200', '5', 4),
(108, NULL, '38', '1000', '5', 6),
(109, NULL, '39', '300', '12', 3),
(110, NULL, '39', '200', '5', 4),
(111, NULL, '39', '1000', '5', 6),
(112, NULL, '40', '300', '12', 3),
(113, NULL, '40', '200', '5', 4),
(114, NULL, '40', '1000', '5', 6),
(115, NULL, '41', '300', '12', 3),
(116, NULL, '41', '200', '5', 4),
(117, NULL, '41', '1000', '5', 6),
(118, NULL, '42', '300', '12', 3),
(119, NULL, '42', '200', '5', 4),
(120, NULL, '42', '1000', '5', 6),
(121, NULL, '43', '300', '12', 3),
(122, NULL, '43', '200', '5', 4),
(123, NULL, '43', '1000', '5', 6),
(124, NULL, '44', '300', '12', 3),
(125, NULL, '44', '200', '5', 4),
(126, NULL, '44', '1000', '5', 6),
(127, NULL, '45', '300', '12', 3),
(128, NULL, '45', '200', '5', 4),
(129, NULL, '45', '1000', '5', 6),
(130, NULL, '46', '300', '12', 3),
(131, NULL, '46', '200', '5', 4),
(132, NULL, '46', '1000', '5', 6),
(133, NULL, '47', '300', '12', 3),
(134, NULL, '47', '200', '5', 4),
(135, NULL, '47', '1000', '5', 6),
(136, NULL, '48', '300', '12', 3),
(137, NULL, '48', '200', '5', 4),
(138, NULL, '48', '1000', '5', 6),
(139, NULL, '49', '300', '12', 3),
(140, NULL, '49', '200', '5', 4),
(141, NULL, '49', '1000', '5', 6),
(142, NULL, '50', '300', '12', 3),
(143, NULL, '50', '200', '5', 4),
(144, NULL, '50', '1000', '5', 6),
(145, NULL, '51', '300', '12', 3),
(146, NULL, '51', '200', '5', 4),
(147, NULL, '51', '1000', '5', 6),
(148, NULL, '52', '300', '12', 3),
(149, NULL, '52', '200', '5', 4),
(150, NULL, '52', '1000', '5', 6),
(151, NULL, '53', '300', '12', 3),
(152, NULL, '53', '200', '5', 4),
(153, NULL, '53', '1000', '5', 6),
(154, NULL, '54', '300', '12', 3),
(155, NULL, '54', '200', '5', 4),
(156, NULL, '54', '1000', '5', 6),
(157, NULL, '55', '300', '12', 3),
(158, NULL, '55', '200', '5', 4),
(159, NULL, '55', '1000', '5', 6),
(160, NULL, '56', '300', '12', 3),
(161, NULL, '56', '200', '5', 4),
(162, NULL, '56', '1000', '5', 6),
(163, NULL, '57', '300', '12', 3),
(164, NULL, '57', '200', '5', 4),
(165, NULL, '57', '1000', '5', 6),
(166, NULL, '58', '300', '12', 3),
(167, NULL, '58', '200', '5', 4),
(168, NULL, '58', '1000', '5', 6),
(169, NULL, '59', '300', '12', 3),
(170, NULL, '59', '200', '5', 4),
(171, NULL, '59', '1000', '5', 6),
(172, NULL, '60', '300', '12', 3),
(173, NULL, '60', '200', '5', 4),
(174, NULL, '60', '1000', '5', 6),
(175, NULL, '61', '300', '12', 3),
(176, NULL, '61', '200', '5', 4),
(177, NULL, '61', '1000', '5', 6),
(178, NULL, '62', '300', '12', 3),
(179, NULL, '62', '200', '5', 4),
(180, NULL, '62', '1000', '5', 6),
(181, '21', '63', '300', '12', 3),
(182, '21', '63', '200', '5', 4),
(183, '21', '63', '1000', '5', 6),
(184, NULL, '64', '300', '12', 3),
(185, NULL, '64', '200', '5', 4),
(186, NULL, '64', '1000', '5', 6),
(187, NULL, '65', '300', '12', 3),
(188, NULL, '65', '200', '5', 4),
(189, NULL, '65', '1000', '5', 6),
(190, '28', NULL, '300', '12', 3),
(191, '28', NULL, '200', '5', 4),
(192, '28', NULL, '1000', '5', 6),
(193, '29', NULL, '300', '12', 3),
(194, '29', NULL, '200', '5', 4),
(195, '29', NULL, '1000', '5', 6),
(196, '30', NULL, '300', '12', 3),
(197, '30', NULL, '200', '5', 4),
(198, '30', NULL, '1000', '5', 6),
(199, '31', NULL, '300', '12', 3),
(200, '31', NULL, '200', '5', 4),
(201, '31', NULL, '1000', '5', 6),
(202, '32', NULL, '300', '12', 3),
(203, '32', NULL, '200', '5', 4),
(204, '32', NULL, '1000', '5', 6),
(205, '33', NULL, '300', '12', 3),
(206, '33', NULL, '200', '5', 4),
(207, '33', NULL, '1000', '5', 6),
(208, '34', NULL, '300', '12', 3),
(209, '34', NULL, '200', '5', 4),
(210, '34', NULL, '1000', '5', 6),
(211, '35', NULL, '300', '12', 3),
(212, '35', NULL, '200', '5', 4),
(213, '35', NULL, '1000', '5', 6),
(214, '36', NULL, '300', '12', 3),
(215, '36', NULL, '200', '5', 4),
(216, '36', NULL, '1000', '5', 6),
(217, '37', NULL, '300', '12', 3),
(218, '37', NULL, '200', '5', 4),
(219, '37', NULL, '1000', '5', 6),
(220, '38', NULL, '300', '12', 3),
(221, '38', NULL, '200', '5', 4),
(222, '38', NULL, '1000', '5', 6),
(223, '39', NULL, '300', '12', 3),
(224, '39', NULL, '200', '5', 4),
(225, '39', NULL, '1000', '5', 6),
(226, '40', NULL, '300', '12', 3),
(227, '40', NULL, '200', '5', 4),
(228, '40', NULL, '1000', '5', 6);

-- --------------------------------------------------------

--
-- Table structure for table `airapanel_payemethistory`
--

CREATE TABLE `airapanel_payemethistory` (
  `id` int(11) NOT NULL,
  `invoice_id` varchar(12) COLLATE utf16_unicode_ci DEFAULT NULL,
  `date_of_payement` datetime(6) NOT NULL,
  `amount` varchar(12) COLLATE utf16_unicode_ci DEFAULT NULL,
  `description` varchar(120) COLLATE utf16_unicode_ci DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf16 COLLATE=utf16_unicode_ci;

--
-- Dumping data for table `airapanel_payemethistory`
--

INSERT INTO `airapanel_payemethistory` (`id`, `invoice_id`, `date_of_payement`, `amount`, `description`) VALUES
(25, '28', '2019-12-07 08:08:14.557717', '1023.2', 'advance'),
(26, '29', '2019-12-07 08:08:23.895381', '1023.2', 'advance'),
(23, '26', '2019-12-07 08:04:00.750329', '1023.2', 'advance'),
(22, '25', '2019-12-07 07:51:12.634080', '1023.2', 'advance'),
(20, '23', '2019-12-07 07:37:45.034842', '1023.2', 'advance'),
(21, '24', '2019-12-07 07:37:56.501500', '1023.2', 'advance'),
(19, '22', '2019-12-07 07:32:48.243526', '1023.2', 'advance'),
(18, NULL, '2019-12-07 13:01:45.965543', '1023.2', 'advance'),
(27, '30', '2019-01-30 00:00:00.000000', '500.0', NULL),
(28, '30', '2019-01-30 00:00:00.000000', '500.0', NULL),
(29, '30', '2019-01-30 00:00:00.000000', '500.0', NULL),
(30, '29', '2019-01-30 00:00:00.000000', '500.0', NULL),
(31, '29', '2019-01-30 00:00:00.000000', '23000.0', NULL),
(32, '29', '2019-01-30 00:00:00.000000', '500.0', NULL),
(33, '40', '2019-12-19 07:29:43.406288', '3000.0', 'advance');

-- --------------------------------------------------------

--
-- Table structure for table `airapanel_products`
--

CREATE TABLE `airapanel_products` (
  `id` int(11) NOT NULL,
  `pdt` varchar(100) COLLATE utf16_unicode_ci NOT NULL,
  `name` varchar(120) COLLATE utf16_unicode_ci NOT NULL,
  `hsn_code` varchar(120) COLLATE utf16_unicode_ci DEFAULT NULL,
  `hsn_group` varchar(120) COLLATE utf16_unicode_ci DEFAULT NULL,
  `item_name` varchar(120) COLLATE utf16_unicode_ci DEFAULT NULL,
  `mrp` varchar(12) COLLATE utf16_unicode_ci DEFAULT NULL,
  `wholesale` varchar(12) COLLATE utf16_unicode_ci DEFAULT NULL,
  `sp` varchar(12) COLLATE utf16_unicode_ci DEFAULT NULL,
  `retail` varchar(12) COLLATE utf16_unicode_ci DEFAULT NULL,
  `branch` varchar(12) COLLATE utf16_unicode_ci DEFAULT NULL,
  `loading_charge` varchar(12) COLLATE utf16_unicode_ci DEFAULT NULL,
  `is_active` int(11) NOT NULL,
  `common_name` varchar(12) COLLATE utf16_unicode_ci DEFAULT NULL,
  `reorder_level` int(11) DEFAULT NULL,
  `rack` varchar(12) COLLATE utf16_unicode_ci DEFAULT NULL,
  `max_order_level` varchar(12) COLLATE utf16_unicode_ci DEFAULT NULL,
  `tax_group` varchar(12) COLLATE utf16_unicode_ci DEFAULT NULL,
  `tax_schedule` varchar(12) COLLATE utf16_unicode_ci DEFAULT NULL,
  `gst` varchar(12) COLLATE utf16_unicode_ci DEFAULT NULL,
  `sgst` varchar(12) COLLATE utf16_unicode_ci DEFAULT NULL,
  `igst` varchar(12) COLLATE utf16_unicode_ci DEFAULT NULL,
  `cgst` varchar(12) COLLATE utf16_unicode_ci DEFAULT NULL,
  `cess` varchar(12) COLLATE utf16_unicode_ci DEFAULT NULL,
  `additional_cess` varchar(12) COLLATE utf16_unicode_ci DEFAULT NULL,
  `second_name` varchar(12) COLLATE utf16_unicode_ci DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf16 COLLATE=utf16_unicode_ci;

--
-- Dumping data for table `airapanel_products`
--

INSERT INTO `airapanel_products` (`id`, `pdt`, `name`, `hsn_code`, `hsn_group`, `item_name`, `mrp`, `wholesale`, `sp`, `retail`, `branch`, `loading_charge`, `is_active`, `common_name`, `reorder_level`, `rack`, `max_order_level`, `tax_group`, `tax_schedule`, `gst`, `sgst`, `igst`, `cgst`, `cess`, `additional_cess`, `second_name`) VALUES
(2, 'AIRA100000', 'i7processor', 'hsncode', 'hsngrp', 'itemname', '200', '200', NULL, NULL, NULL, NULL, 1, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(3, 'AIRA100002', 'ram1gb', 'hsncode', 'hsngrp', 'itemname', '200', '200', NULL, NULL, NULL, NULL, 1, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(4, 'AIRA100003', 'ram2gb', 'hsncode', 'hsngrp', 'itemname', '200', '200', NULL, NULL, NULL, NULL, 1, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(5, 'AIRA100004', 'ram4gb', 'hsncode', 'hsngrp', 'itemname', '200', '200', NULL, NULL, NULL, NULL, 1, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL),
(6, 'AIRA100005', 'ram8gb', 'hsncode', 'hsngrp', 'itemname', '200', '200', NULL, NULL, NULL, NULL, 1, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `airapanel_products_category`
--

CREATE TABLE `airapanel_products_category` (
  `id` int(11) NOT NULL,
  `products_id` int(11) NOT NULL,
  `categories_id` int(11) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf16 COLLATE=utf16_unicode_ci;

--
-- Dumping data for table `airapanel_products_category`
--

INSERT INTO `airapanel_products_category` (`id`, `products_id`, `categories_id`) VALUES
(2, 2, 1),
(3, 3, 1),
(4, 4, 1),
(5, 5, 1),
(6, 6, 1);

-- --------------------------------------------------------

--
-- Table structure for table `airapanel_products_manufaturer`
--

CREATE TABLE `airapanel_products_manufaturer` (
  `id` int(11) NOT NULL,
  `products_id` int(11) NOT NULL,
  `companies_id` int(11) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf16 COLLATE=utf16_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `airapanel_products_subcategory`
--

CREATE TABLE `airapanel_products_subcategory` (
  `id` int(11) NOT NULL,
  `products_id` int(11) NOT NULL,
  `subcategories_id` int(11) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf16 COLLATE=utf16_unicode_ci;

--
-- Dumping data for table `airapanel_products_subcategory`
--

INSERT INTO `airapanel_products_subcategory` (`id`, `products_id`, `subcategories_id`) VALUES
(2, 2, 1),
(3, 3, 1),
(4, 4, 1),
(5, 5, 1),
(6, 6, 1);

-- --------------------------------------------------------

--
-- Table structure for table `airapanel_products_unit`
--

CREATE TABLE `airapanel_products_unit` (
  `id` int(11) NOT NULL,
  `products_id` int(11) NOT NULL,
  `units_id` int(11) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf16 COLLATE=utf16_unicode_ci;

--
-- Dumping data for table `airapanel_products_unit`
--

INSERT INTO `airapanel_products_unit` (`id`, `products_id`, `units_id`) VALUES
(1, 2, 1),
(2, 3, 1),
(3, 4, 1),
(4, 5, 1),
(5, 6, 1);

-- --------------------------------------------------------

--
-- Table structure for table `airapanel_purchasecontracts`
--

CREATE TABLE `airapanel_purchasecontracts` (
  `id` int(11) NOT NULL,
  `contract_id` varchar(20) COLLATE utf16_unicode_ci DEFAULT NULL,
  `created` datetime(6) NOT NULL,
  `end_date` datetime(6) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf16 COLLATE=utf16_unicode_ci;

--
-- Dumping data for table `airapanel_purchasecontracts`
--

INSERT INTO `airapanel_purchasecontracts` (`id`, `contract_id`, `created`, `end_date`) VALUES
(63, 'purchase_contract_id', '2019-12-13 04:38:43.716274', '2019-12-09 00:00:00.000000'),
(62, 'purchase_contract_id', '2019-12-13 04:28:45.053982', '2019-12-09 00:00:00.000000'),
(61, 'purchase_contract_id', '2019-12-13 04:28:43.765577', '2019-12-09 00:00:00.000000'),
(60, 'purchase_contract_id', '2019-12-13 04:28:42.728283', '2019-12-09 00:00:00.000000'),
(59, 'purchase_contract_id', '2019-12-13 04:28:41.435323', '2019-12-09 00:00:00.000000'),
(58, 'purchase_contract_id', '2019-12-13 04:28:39.505277', '2019-12-09 00:00:00.000000'),
(57, 'purchase_contract_id', '2019-12-13 04:28:09.892517', '2019-12-09 00:00:00.000000'),
(56, 'purchase_contract_id', '2019-12-13 04:28:07.425102', '2019-12-09 00:00:00.000000'),
(55, 'purchase_contract_id', '2019-12-13 04:28:05.502931', '2019-12-09 00:00:00.000000'),
(54, 'purchase_contract_id', '2019-12-13 04:28:02.832869', '2019-12-09 00:00:00.000000'),
(53, 'purchase_contract_id', '2019-12-12 12:34:45.689437', '2019-12-09 00:00:00.000000');

-- --------------------------------------------------------

--
-- Table structure for table `airapanel_purchasecontracts_items`
--

CREATE TABLE `airapanel_purchasecontracts_items` (
  `id` int(11) NOT NULL,
  `purchasecontracts_id` int(11) NOT NULL,
  `purchase_items_relation_id` int(11) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf16 COLLATE=utf16_unicode_ci;

--
-- Dumping data for table `airapanel_purchasecontracts_items`
--

INSERT INTO `airapanel_purchasecontracts_items` (`id`, `purchasecontracts_id`, `purchase_items_relation_id`) VALUES
(33, 57, 193),
(32, 57, 194),
(31, 57, 195),
(30, 56, 190),
(29, 56, 191),
(28, 56, 192),
(27, 55, 187),
(26, 55, 188),
(25, 55, 189),
(24, 54, 184),
(23, 54, 185),
(22, 54, 186),
(21, 53, 181),
(20, 53, 182),
(19, 53, 183),
(34, 58, 198),
(35, 58, 197),
(36, 58, 196),
(37, 59, 201),
(38, 59, 200),
(39, 59, 199),
(40, 60, 204),
(41, 60, 203),
(42, 60, 202),
(43, 61, 207),
(44, 61, 206),
(45, 61, 205),
(46, 62, 208),
(47, 62, 209),
(48, 62, 210),
(49, 63, 211),
(50, 63, 212),
(51, 63, 213);

-- --------------------------------------------------------

--
-- Table structure for table `airapanel_purchasecontracts_vendors`
--

CREATE TABLE `airapanel_purchasecontracts_vendors` (
  `id` int(11) NOT NULL,
  `purchasecontracts_id` int(11) NOT NULL,
  `customers_id` int(11) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf16 COLLATE=utf16_unicode_ci;

--
-- Dumping data for table `airapanel_purchasecontracts_vendors`
--

INSERT INTO `airapanel_purchasecontracts_vendors` (`id`, `purchasecontracts_id`, `customers_id`) VALUES
(106, 63, 7),
(105, 63, 6),
(104, 62, 7),
(103, 62, 6),
(102, 61, 7),
(101, 61, 6),
(100, 60, 7),
(99, 60, 6),
(98, 59, 7),
(97, 59, 6),
(96, 58, 7),
(95, 58, 6),
(94, 57, 7),
(93, 57, 6),
(92, 56, 7),
(91, 56, 6),
(90, 55, 7),
(89, 55, 6),
(88, 54, 7),
(87, 54, 6),
(86, 53, 7),
(85, 53, 6);

-- --------------------------------------------------------

--
-- Table structure for table `airapanel_purchaseorder`
--

CREATE TABLE `airapanel_purchaseorder` (
  `id` int(11) NOT NULL,
  `contract_referance` varchar(20) COLLATE utf16_unicode_ci DEFAULT NULL,
  `created` datetime(6) NOT NULL,
  `status` varchar(20) COLLATE utf16_unicode_ci DEFAULT NULL,
  `billing_status` varchar(20) COLLATE utf16_unicode_ci DEFAULT NULL,
  `vendor_referance` varchar(20) COLLATE utf16_unicode_ci DEFAULT NULL,
  `purchase_by` varchar(20) COLLATE utf16_unicode_ci DEFAULT NULL,
  `paid_amount` varchar(12) COLLATE utf16_unicode_ci DEFAULT NULL,
  `total_amount` varchar(12) COLLATE utf16_unicode_ci DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf16 COLLATE=utf16_unicode_ci;

--
-- Dumping data for table `airapanel_purchaseorder`
--

INSERT INTO `airapanel_purchaseorder` (`id`, `contract_referance`, `created`, `status`, `billing_status`, `vendor_referance`, `purchase_by`, `paid_amount`, `total_amount`) VALUES
(1, '21', '2019-12-14 04:24:49.106844', '', '', '', NULL, NULL, NULL),
(2, '21', '2019-12-14 04:25:38.284972', '', '', '', NULL, NULL, NULL),
(3, '21', '2019-12-14 04:26:04.259355', '', '', '', NULL, NULL, NULL),
(4, '21', '2019-12-14 04:30:23.433832', '', '', '', NULL, NULL, NULL),
(5, '21', '2019-12-19 09:57:19.268278', '', '', '', NULL, NULL, NULL),
(6, '21', '2019-12-19 09:58:37.491821', 'paritally_paid', '', '', NULL, '7000.0', '20000');

-- --------------------------------------------------------

--
-- Table structure for table `airapanel_purchaseorder_items`
--

CREATE TABLE `airapanel_purchaseorder_items` (
  `id` int(11) NOT NULL,
  `purchaseorder_id` int(11) NOT NULL,
  `purchase_items_relation_id` int(11) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf16 COLLATE=utf16_unicode_ci;

--
-- Dumping data for table `airapanel_purchaseorder_items`
--

INSERT INTO `airapanel_purchaseorder_items` (`id`, `purchaseorder_id`, `purchase_items_relation_id`) VALUES
(1, 4, 217),
(2, 4, 218),
(3, 4, 219),
(4, 5, 220),
(5, 5, 221),
(6, 5, 222),
(7, 6, 223),
(8, 6, 224),
(9, 6, 225);

-- --------------------------------------------------------

--
-- Table structure for table `airapanel_purchaseorder_payement_history`
--

CREATE TABLE `airapanel_purchaseorder_payement_history` (
  `id` int(11) NOT NULL,
  `purchaseorder_id` int(11) NOT NULL,
  `purchasepayemethistory_id` int(11) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf16 COLLATE=utf16_unicode_ci;

--
-- Dumping data for table `airapanel_purchaseorder_payement_history`
--

INSERT INTO `airapanel_purchaseorder_payement_history` (`id`, `purchaseorder_id`, `purchasepayemethistory_id`) VALUES
(1, 6, 1),
(2, 6, 2),
(3, 6, 3),
(4, 6, 4);

-- --------------------------------------------------------

--
-- Table structure for table `airapanel_purchaseorder_vendors`
--

CREATE TABLE `airapanel_purchaseorder_vendors` (
  `id` int(11) NOT NULL,
  `purchaseorder_id` int(11) NOT NULL,
  `customers_id` int(11) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf16 COLLATE=utf16_unicode_ci;

--
-- Dumping data for table `airapanel_purchaseorder_vendors`
--

INSERT INTO `airapanel_purchaseorder_vendors` (`id`, `purchaseorder_id`, `customers_id`) VALUES
(1, 3, 6),
(2, 4, 6),
(3, 5, 6),
(4, 6, 6);

-- --------------------------------------------------------

--
-- Table structure for table `airapanel_purchasepayemethistory`
--

CREATE TABLE `airapanel_purchasepayemethistory` (
  `id` int(11) NOT NULL,
  `purchase_id` varchar(12) COLLATE utf16_unicode_ci DEFAULT NULL,
  `date_of_payement` datetime(6) NOT NULL,
  `amount` varchar(12) COLLATE utf16_unicode_ci DEFAULT NULL,
  `description` varchar(120) COLLATE utf16_unicode_ci DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf16 COLLATE=utf16_unicode_ci;

--
-- Dumping data for table `airapanel_purchasepayemethistory`
--

INSERT INTO `airapanel_purchasepayemethistory` (`id`, `purchase_id`, `date_of_payement`, `amount`, `description`) VALUES
(1, '6', '2019-12-19 09:58:37.491821', '1000.0', 'advance'),
(2, '6', '2020-01-02 00:00:00.000000', '500.0', NULL),
(3, '6', '2020-01-03 00:00:00.000000', '500.0', NULL),
(4, '6', '2020-01-03 00:00:00.000000', '5000.0', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `airapanel_purchase_items_relation`
--

CREATE TABLE `airapanel_purchase_items_relation` (
  `id` int(11) NOT NULL,
  `contract_id` varchar(20) COLLATE utf16_unicode_ci DEFAULT NULL,
  `purchase_id` varchar(20) COLLATE utf16_unicode_ci DEFAULT NULL,
  `item_price` varchar(20) COLLATE utf16_unicode_ci DEFAULT NULL,
  `tax` varchar(10) COLLATE utf16_unicode_ci DEFAULT NULL,
  `product_Id_id` int(11) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf16 COLLATE=utf16_unicode_ci;

--
-- Dumping data for table `airapanel_purchase_items_relation`
--

INSERT INTO `airapanel_purchase_items_relation` (`id`, `contract_id`, `purchase_id`, `item_price`, `tax`, `product_Id_id`) VALUES
(207, '61', 'Purchase_id_here', NULL, NULL, 6),
(206, '61', 'Purchase_id_here', NULL, NULL, 4),
(205, '61', 'Purchase_id_here', NULL, NULL, 3),
(204, '60', 'Purchase_id_here', NULL, NULL, 6),
(203, '60', 'Purchase_id_here', NULL, NULL, 4),
(202, '60', 'Purchase_id_here', NULL, NULL, 3),
(201, '59', 'Purchase_id_here', NULL, NULL, 6),
(200, '59', 'Purchase_id_here', NULL, NULL, 4),
(199, '59', 'Purchase_id_here', NULL, NULL, 3),
(198, '58', 'Purchase_id_here', NULL, NULL, 6),
(197, '58', 'Purchase_id_here', NULL, NULL, 4),
(196, '58', 'Purchase_id_here', NULL, NULL, 3),
(195, '57', 'Purchase_id_here', NULL, NULL, 6),
(194, '57', 'Purchase_id_here', NULL, NULL, 4),
(193, '57', 'Purchase_id_here', NULL, NULL, 3),
(192, '56', 'Purchase_id_here', NULL, NULL, 6),
(191, '56', 'Purchase_id_here', NULL, NULL, 4),
(190, '56', 'Purchase_id_here', NULL, NULL, 3),
(189, '55', 'Purchase_id_here', NULL, NULL, 6),
(188, '55', 'Purchase_id_here', NULL, NULL, 4),
(187, '55', 'Purchase_id_here', NULL, NULL, 3),
(186, '54', 'Purchase_id_here', NULL, NULL, 6),
(185, '54', 'Purchase_id_here', NULL, NULL, 4),
(184, '54', 'Purchase_id_here', NULL, NULL, 3),
(183, '53', 'Purchase_id_here', NULL, NULL, 6),
(182, '53', 'Purchase_id_here', NULL, NULL, 4),
(181, '53', 'Purchase_id_here', NULL, NULL, 3),
(180, '52', 'Purchase_id_here', NULL, NULL, 6),
(179, '52', 'Purchase_id_here', NULL, NULL, 4),
(178, '52', 'Purchase_id_here', NULL, NULL, 3),
(177, '51', 'Purchase_id_here', NULL, NULL, 6),
(176, '51', 'Purchase_id_here', NULL, NULL, 4),
(175, '51', 'Purchase_id_here', NULL, NULL, 3),
(174, '50', 'Purchase_id_here', NULL, NULL, 6),
(173, '50', 'Purchase_id_here', NULL, NULL, 4),
(172, '50', 'Purchase_id_here', NULL, NULL, 3),
(171, '49', 'Purchase_id_here', NULL, NULL, 6),
(170, '49', 'Purchase_id_here', NULL, NULL, 4),
(169, '49', 'Purchase_id_here', NULL, NULL, 3),
(168, '48', 'Purchase_id_here', NULL, NULL, 6),
(167, '48', 'Purchase_id_here', NULL, NULL, 4),
(166, '48', 'Purchase_id_here', NULL, NULL, 3),
(165, '46', 'Purchase_id_here', NULL, NULL, 6),
(164, '46', 'Purchase_id_here', NULL, NULL, 4),
(163, '46', 'Purchase_id_here', NULL, NULL, 3),
(162, '45', 'Purchase_id_here', NULL, NULL, 6),
(161, '45', 'Purchase_id_here', NULL, NULL, 4),
(160, '45', 'Purchase_id_here', NULL, NULL, 3),
(159, '44', 'Purchase_id_here', NULL, NULL, 6),
(158, '44', 'Purchase_id_here', NULL, NULL, 4),
(157, '44', 'Purchase_id_here', NULL, NULL, 3),
(156, '43', 'Purchase_id_here', NULL, NULL, 6),
(155, '43', 'Purchase_id_here', NULL, NULL, 4),
(154, '43', 'Purchase_id_here', NULL, NULL, 3),
(153, '41', 'Purchase_id_here', NULL, NULL, 6),
(152, '41', 'Purchase_id_here', NULL, NULL, 4),
(151, '41', 'Purchase_id_here', NULL, NULL, 3),
(150, '40', 'Purchase_id_here', NULL, NULL, 6),
(149, '40', 'Purchase_id_here', NULL, NULL, 4),
(148, '40', 'Purchase_id_here', NULL, NULL, 3),
(147, '39', 'Purchase_id_here', NULL, NULL, 6),
(146, '39', 'Purchase_id_here', NULL, NULL, 4),
(145, '39', 'Purchase_id_here', NULL, NULL, 3),
(144, '38', 'Purchase_id_here', NULL, NULL, 6),
(143, '38', 'Purchase_id_here', NULL, NULL, 4),
(142, '38', 'Purchase_id_here', NULL, NULL, 3),
(141, '37', 'Purchase_id_here', NULL, NULL, 6),
(140, '37', 'Purchase_id_here', NULL, NULL, 4),
(139, '37', 'Purchase_id_here', NULL, NULL, 3),
(208, '62', 'Purchase_id_here', NULL, NULL, 3),
(209, '62', 'Purchase_id_here', NULL, NULL, 4),
(210, '62', 'Purchase_id_here', NULL, NULL, 6),
(211, '63', 'Purchase_id_here', NULL, NULL, 3),
(212, '63', 'Purchase_id_here', NULL, NULL, 4),
(213, '63', 'Purchase_id_here', NULL, NULL, 6),
(214, '64', 'Purchase_id_here', NULL, NULL, 3),
(215, '64', 'Purchase_id_here', NULL, NULL, 4),
(216, '64', 'Purchase_id_here', NULL, NULL, 6),
(217, '4', 'Purchase_id_here', '300', '12', 3),
(218, '4', 'Purchase_id_here', '200', '5', 4),
(219, '4', 'Purchase_id_here', '1000', '5', 6),
(220, '5', 'Purchase_id_here', '300', '12', 3),
(221, '5', 'Purchase_id_here', '200', '5', 4),
(222, '5', 'Purchase_id_here', '1000', '5', 6),
(223, '6', 'Purchase_id_here', '300.0', '12', 3),
(224, '6', 'Purchase_id_here', '200.0', '5', 4),
(225, '6', 'Purchase_id_here', '1000.0', '5', 6),
(226, '7', 'Purchase_id_here', '300.0', '12', 3),
(227, '7', 'Purchase_id_here', '200.0', '5', 4),
(228, '7', 'Purchase_id_here', '1000.0', '5', 6);

-- --------------------------------------------------------

--
-- Table structure for table `airapanel_sales`
--

CREATE TABLE `airapanel_sales` (
  `id` int(11) NOT NULL,
  `created` datetime(6) NOT NULL,
  `due_date` datetime(6) NOT NULL,
  `total_amount` varchar(12) COLLATE utf16_unicode_ci DEFAULT NULL,
  `status` varchar(20) COLLATE utf16_unicode_ci DEFAULT NULL,
  `invoice_status` varchar(20) COLLATE utf16_unicode_ci DEFAULT NULL,
  `company_id` int(11) DEFAULT NULL,
  `customer_id` int(11) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf16 COLLATE=utf16_unicode_ci;

--
-- Dumping data for table `airapanel_sales`
--

INSERT INTO `airapanel_sales` (`id`, `created`, `due_date`, `total_amount`, `status`, `invoice_status`, `company_id`, `customer_id`) VALUES
(7, '2019-11-30 12:44:37.949023', '2019-02-26 00:00:00.000000', '25000', 'Quotation', 'To invoice', 11, 6),
(8, '2019-11-30 12:46:19.815760', '2019-02-26 00:00:00.000000', '25000', 'Quotation', 'To invoice', 11, 6),
(9, '2019-11-30 12:47:24.273415', '2019-02-26 00:00:00.000000', '25000', 'Quotation', 'To invoice', 11, 6),
(10, '2019-12-04 06:38:00.875787', '2019-02-26 00:00:00.000000', '25000', 'Sale order', 'To invoice', 11, 6),
(11, '2019-12-04 07:05:30.023730', '2019-02-26 00:00:00.000000', '25000', 'Sale order', 'To invoice', 11, 6),
(12, '2019-12-04 07:07:21.409577', '2019-02-26 00:00:00.000000', '25000', 'Sale order', 'To invoice', 11, 6),
(13, '2019-12-04 09:17:27.097304', '2019-02-26 00:00:00.000000', '25000', 'Sale order', 'To invoice', 11, 6),
(14, '2019-12-04 09:33:14.285635', '2019-02-26 00:00:00.000000', '25000', 'Sale order', 'To invoice', 11, 6),
(15, '2019-12-04 09:33:18.150949', '2019-02-26 00:00:00.000000', '25000', 'Sale order', 'To invoice', 11, 6),
(16, '2019-12-04 09:33:19.218550', '2019-02-26 00:00:00.000000', '25000', 'Sale order', 'To invoice', 11, 6),
(17, '2019-12-04 09:33:20.157274', '2019-02-26 00:00:00.000000', '25000', 'Sale order', 'To invoice', 11, 6),
(18, '2019-12-04 09:34:11.496643', '2019-02-26 00:00:00.000000', '25000', 'Sale order', 'To invoice', 11, 6),
(19, '2019-12-04 09:34:16.018299', '2019-02-26 00:00:00.000000', '25000', 'Sale order', 'To invoice', 11, 6),
(20, '2019-12-04 09:34:19.005426', '2019-02-26 00:00:00.000000', '25000', 'Sale order', 'To invoice', 11, 6),
(21, '2019-12-04 09:34:21.113957', '2019-02-26 00:00:00.000000', '25000', 'Sale order', 'To invoice', 11, 6),
(22, '2019-12-04 09:34:22.197172', '2019-02-26 00:00:00.000000', '25000', 'Sale order', 'To invoice', 11, 6),
(23, '2019-12-04 09:34:22.994889', '2019-02-26 00:00:00.000000', '25000', 'Sale order', 'To invoice', 11, 6),
(24, '2019-12-04 09:35:11.882054', '2019-02-26 00:00:00.000000', '25000', 'Sale order', 'To invoice', 11, 6),
(25, '2019-12-04 09:35:13.064898', '2019-02-26 00:00:00.000000', '25000', 'Sale order', 'To invoice', 11, 6),
(26, '2019-12-04 09:35:13.885448', '2019-02-26 00:00:00.000000', '25000', 'Sale order', 'To invoice', 11, 6),
(27, '2019-12-04 09:35:14.685307', '2019-02-26 00:00:00.000000', '25000', 'Sale order', 'To invoice', 11, 6),
(28, '2019-12-04 09:35:15.417821', '2019-02-26 00:00:00.000000', '25000', 'Sale order', 'To invoice', 11, 6),
(29, '2019-12-04 09:35:16.167816', '2019-02-26 00:00:00.000000', '25000', 'Sale order', 'To invoice', 11, 6),
(30, '2019-12-04 09:35:16.937759', '2019-02-26 00:00:00.000000', '25000', 'Sale order', 'To invoice', 11, 6),
(31, '2019-12-04 09:35:17.998689', '2019-02-26 00:00:00.000000', '25000', 'Sale order', 'To invoice', 11, 6),
(32, '2019-12-04 09:35:18.855102', '2019-02-26 00:00:00.000000', '25000', 'Sale order', 'To invoice', 11, 6),
(33, '2019-12-04 09:35:43.242581', '2019-02-26 00:00:00.000000', '25000', 'Sale order', 'To invoice', 11, 6),
(34, '2019-12-04 09:35:44.026485', '2019-02-26 00:00:00.000000', '25000', 'Sale order', 'To invoice', 11, 6),
(35, '2019-12-04 09:35:44.716163', '2019-02-26 00:00:00.000000', '25000', 'Sale order', 'To invoice', 11, 6),
(36, '2019-12-04 09:35:45.320393', '2019-02-26 00:00:00.000000', '25000', 'Sale order', 'To invoice', 11, 6),
(37, '2019-12-04 09:35:46.163249', '2019-02-26 00:00:00.000000', '25000', 'Sale order', 'To invoice', 11, 6),
(38, '2019-12-04 09:35:46.824201', '2019-02-26 00:00:00.000000', '25000', 'Sale order', 'To invoice', 11, 6),
(39, '2019-12-04 09:35:47.625207', '2019-02-26 00:00:00.000000', '25000', 'Sale order', 'To invoice', 11, 6),
(40, '2019-12-04 09:35:48.093905', '2019-02-26 00:00:00.000000', '25000', 'Sale order', 'To invoice', 11, 6),
(41, '2019-12-04 09:35:48.737862', '2019-02-26 00:00:00.000000', '25000', 'Sale order', 'To invoice', 11, 6),
(42, '2019-12-04 09:35:49.332266', '2019-02-26 00:00:00.000000', '25000', 'Sale order', 'To invoice', 11, 6),
(43, '2019-12-04 09:35:49.943340', '2019-02-26 00:00:00.000000', '25000', 'Sale order', 'To invoice', 11, 6),
(44, '2019-12-04 09:35:50.553714', '2019-02-26 00:00:00.000000', '25000', 'Sale order', 'To invoice', 11, 6),
(45, '2019-12-04 09:35:51.181442', '2019-02-26 00:00:00.000000', '25000', 'Sale order', 'To invoice', 11, 6),
(46, '2019-12-04 09:35:51.685442', '2019-02-26 00:00:00.000000', '25000', 'Sale order', 'To invoice', 11, 6),
(47, '2019-12-04 09:35:52.312735', '2019-02-26 00:00:00.000000', '25000', 'Sale order', 'To invoice', 11, 6),
(48, '2019-12-04 09:35:52.904776', '2019-02-26 00:00:00.000000', '25000', 'Sale order', 'To invoice', 11, 6),
(49, '2019-12-04 09:35:53.516725', '2019-02-26 00:00:00.000000', '25000', 'Sale order', 'To invoice', 11, 6),
(50, '2019-12-04 09:35:54.196484', '2019-02-26 00:00:00.000000', '25000', 'Sale order', 'To invoice', 11, 6),
(51, '2019-12-04 09:35:54.689777', '2019-02-26 00:00:00.000000', '25000', 'Sale order', 'To invoice', 11, 6),
(52, '2019-12-04 09:35:55.270625', '2019-02-26 00:00:00.000000', '25000', 'Sale order', 'To invoice', 11, 6),
(53, '2019-12-04 09:35:55.797566', '2019-02-26 00:00:00.000000', '25000', 'Sale order', 'To invoice', 11, 6),
(54, '2019-12-05 07:31:55.546057', '2019-02-26 00:00:00.000000', '25000', 'Sale order', 'To invoice', 11, 6),
(55, '2019-12-05 07:31:59.055214', '2019-02-26 00:00:00.000000', '25000', 'Sale order', 'To invoice', 11, 6),
(56, '2019-12-05 07:32:00.807369', '2019-02-26 00:00:00.000000', '25000', 'Sale order', 'To invoice', 11, 6),
(57, '2019-12-05 07:32:02.018840', '2019-02-26 00:00:00.000000', '25000', 'Sale order', 'To invoice', 11, 6),
(58, '2019-12-05 07:32:03.027992', '2019-02-26 00:00:00.000000', '25000', 'Sale order', 'To invoice', 11, 6),
(59, '2019-12-05 07:32:04.092810', '2019-02-26 00:00:00.000000', '25000', 'Sale order', 'To invoice', 11, 6),
(60, '2019-12-05 07:32:05.236725', '2019-02-26 00:00:00.000000', '25000', 'Sale order', 'To invoice', 11, 6),
(61, '2019-12-05 07:32:06.193773', '2019-02-26 00:00:00.000000', '25000', 'Sale order', 'To invoice', 11, 6),
(62, '2019-12-05 07:32:07.084878', '2019-02-26 00:00:00.000000', '25000', 'Sale order', 'To invoice', 11, 6),
(63, '2019-12-05 07:32:09.773116', '2019-03-28 00:00:00.000000', '25000', 'Sale order', 'Fully invoiced', 11, 6);

-- --------------------------------------------------------

--
-- Table structure for table `airapanel_sales_history`
--

CREATE TABLE `airapanel_sales_history` (
  `id` int(11) NOT NULL,
  `sales_id` int(11) NOT NULL,
  `history_id` int(11) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf16 COLLATE=utf16_unicode_ci;

--
-- Dumping data for table `airapanel_sales_history`
--

INSERT INTO `airapanel_sales_history` (`id`, `sales_id`, `history_id`) VALUES
(1, 12, 2),
(2, 13, 3),
(3, 14, 4),
(4, 15, 5),
(5, 16, 6),
(6, 17, 7),
(7, 18, 8),
(8, 19, 9),
(9, 20, 10),
(10, 21, 11),
(11, 22, 12),
(12, 23, 13),
(13, 24, 14),
(14, 25, 15),
(15, 26, 16),
(16, 27, 17),
(17, 28, 18),
(18, 29, 19),
(19, 30, 20),
(20, 31, 21),
(21, 32, 22),
(22, 33, 23),
(23, 34, 24),
(24, 35, 25),
(25, 36, 26),
(26, 37, 27),
(27, 38, 28),
(28, 39, 29),
(29, 40, 30),
(30, 41, 31),
(31, 42, 32),
(32, 43, 33),
(33, 44, 34),
(34, 45, 35),
(35, 46, 36),
(36, 47, 37),
(37, 48, 38),
(38, 49, 39),
(39, 50, 40),
(40, 51, 41),
(41, 52, 42),
(42, 53, 43),
(43, 54, 44),
(44, 55, 45),
(45, 56, 46),
(46, 57, 47),
(47, 58, 48),
(48, 59, 49),
(49, 60, 50),
(50, 61, 51),
(51, 62, 52),
(52, 63, 53),
(65, 63, 66),
(64, 63, 65),
(63, 63, 64),
(62, 63, 63),
(61, 63, 62);

-- --------------------------------------------------------

--
-- Table structure for table `airapanel_sales_items`
--

CREATE TABLE `airapanel_sales_items` (
  `id` int(11) NOT NULL,
  `sales_id` int(11) NOT NULL,
  `items_relation_id` int(11) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf16 COLLATE=utf16_unicode_ci;

--
-- Dumping data for table `airapanel_sales_items`
--

INSERT INTO `airapanel_sales_items` (`id`, `sales_id`, `items_relation_id`) VALUES
(1, 7, 13),
(2, 7, 14),
(3, 7, 15),
(4, 8, 16),
(5, 8, 17),
(6, 8, 18),
(7, 9, 19),
(8, 9, 20),
(9, 9, 21),
(10, 10, 22),
(11, 10, 23),
(12, 10, 24),
(13, 11, 25),
(14, 11, 26),
(15, 11, 27),
(16, 12, 28),
(17, 12, 29),
(18, 12, 30),
(19, 13, 31),
(20, 13, 32),
(21, 13, 33),
(22, 14, 34),
(23, 14, 35),
(24, 14, 36),
(25, 15, 37),
(26, 15, 38),
(27, 15, 39),
(28, 16, 40),
(29, 16, 41),
(30, 16, 42),
(31, 17, 43),
(32, 17, 44),
(33, 17, 45),
(34, 18, 46),
(35, 18, 47),
(36, 18, 48),
(37, 19, 49),
(38, 19, 50),
(39, 19, 51),
(40, 20, 52),
(41, 20, 53),
(42, 20, 54),
(43, 21, 55),
(44, 21, 56),
(45, 21, 57),
(46, 22, 58),
(47, 22, 59),
(48, 22, 60),
(49, 23, 61),
(50, 23, 62),
(51, 23, 63),
(52, 24, 64),
(53, 24, 65),
(54, 24, 66),
(55, 25, 67),
(56, 25, 68),
(57, 25, 69),
(58, 26, 70),
(59, 26, 71),
(60, 26, 72),
(61, 27, 73),
(62, 27, 74),
(63, 27, 75),
(64, 28, 76),
(65, 28, 77),
(66, 28, 78),
(67, 29, 79),
(68, 29, 80),
(69, 29, 81),
(70, 30, 82),
(71, 30, 83),
(72, 30, 84),
(73, 31, 85),
(74, 31, 86),
(75, 31, 87),
(76, 32, 88),
(77, 32, 89),
(78, 32, 90),
(79, 33, 91),
(80, 33, 92),
(81, 33, 93),
(82, 34, 94),
(83, 34, 95),
(84, 34, 96),
(85, 35, 97),
(86, 35, 98),
(87, 35, 99),
(88, 36, 100),
(89, 36, 101),
(90, 36, 102),
(91, 37, 103),
(92, 37, 104),
(93, 37, 105),
(94, 38, 106),
(95, 38, 107),
(96, 38, 108),
(97, 39, 109),
(98, 39, 110),
(99, 39, 111),
(100, 40, 112),
(101, 40, 113),
(102, 40, 114),
(103, 41, 115),
(104, 41, 116),
(105, 41, 117),
(106, 42, 118),
(107, 42, 119),
(108, 42, 120),
(109, 43, 121),
(110, 43, 122),
(111, 43, 123),
(112, 44, 124),
(113, 44, 125),
(114, 44, 126),
(115, 45, 127),
(116, 45, 128),
(117, 45, 129),
(118, 46, 130),
(119, 46, 131),
(120, 46, 132),
(121, 47, 133),
(122, 47, 134),
(123, 47, 135),
(124, 48, 136),
(125, 48, 137),
(126, 48, 138),
(127, 49, 139),
(128, 49, 140),
(129, 49, 141),
(130, 50, 142),
(131, 50, 143),
(132, 50, 144),
(133, 51, 145),
(134, 51, 146),
(135, 51, 147),
(136, 52, 148),
(137, 52, 149),
(138, 52, 150),
(139, 53, 151),
(140, 53, 152),
(141, 53, 153),
(142, 54, 154),
(143, 54, 155),
(144, 54, 156),
(145, 55, 157),
(146, 55, 158),
(147, 55, 159),
(148, 56, 160),
(149, 56, 161),
(150, 56, 162),
(151, 57, 163),
(152, 57, 164),
(153, 57, 165),
(154, 58, 166),
(155, 58, 167),
(156, 58, 168),
(157, 59, 169),
(158, 59, 170),
(159, 59, 171),
(160, 60, 172),
(161, 60, 173),
(162, 60, 174),
(163, 61, 175),
(164, 61, 176),
(165, 61, 177),
(166, 62, 178),
(167, 62, 179),
(168, 62, 180),
(169, 63, 181),
(170, 63, 182),
(171, 63, 183);

-- --------------------------------------------------------

--
-- Table structure for table `airapanel_subcategories`
--

CREATE TABLE `airapanel_subcategories` (
  `id` int(11) NOT NULL,
  `name` varchar(120) COLLATE utf16_unicode_ci NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf16 COLLATE=utf16_unicode_ci;

--
-- Dumping data for table `airapanel_subcategories`
--

INSERT INTO `airapanel_subcategories` (`id`, `name`) VALUES
(1, 'computer'),
(2, 'stationary'),
(3, 'vegetable'),
(4, 'fruit'),
(5, 'dress');

-- --------------------------------------------------------

--
-- Table structure for table `airapanel_units`
--

CREATE TABLE `airapanel_units` (
  `id` int(11) NOT NULL,
  `name` varchar(120) COLLATE utf16_unicode_ci NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf16 COLLATE=utf16_unicode_ci;

--
-- Dumping data for table `airapanel_units`
--

INSERT INTO `airapanel_units` (`id`, `name`) VALUES
(1, 'nos'),
(2, 'unit'),
(3, 'kg'),
(4, 'g'),
(5, 'liter');

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) COLLATE utf16_unicode_ci NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf16 COLLATE=utf16_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf16 COLLATE=utf16_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) COLLATE utf16_unicode_ci NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) COLLATE utf16_unicode_ci NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf16 COLLATE=utf16_unicode_ci;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add categories', 7, 'add_categories'),
(26, 'Can change categories', 7, 'change_categories'),
(27, 'Can delete categories', 7, 'delete_categories'),
(28, 'Can view categories', 7, 'view_categories'),
(29, 'Can add companies', 8, 'add_companies'),
(30, 'Can change companies', 8, 'change_companies'),
(31, 'Can delete companies', 8, 'delete_companies'),
(32, 'Can view companies', 8, 'view_companies'),
(33, 'Can add sub categories', 9, 'add_subcategories'),
(34, 'Can change sub categories', 9, 'change_subcategories'),
(35, 'Can delete sub categories', 9, 'delete_subcategories'),
(36, 'Can view sub categories', 9, 'view_subcategories'),
(37, 'Can add units', 10, 'add_units'),
(38, 'Can change units', 10, 'change_units'),
(39, 'Can delete units', 10, 'delete_units'),
(40, 'Can view units', 10, 'view_units'),
(41, 'Can add products', 11, 'add_products'),
(42, 'Can change products', 11, 'change_products'),
(43, 'Can delete products', 11, 'delete_products'),
(44, 'Can view products', 11, 'view_products'),
(45, 'Can add customers', 12, 'add_customers'),
(46, 'Can change customers', 12, 'change_customers'),
(47, 'Can delete customers', 12, 'delete_customers'),
(48, 'Can view customers', 12, 'view_customers'),
(49, 'Can add items invoice', 13, 'add_itemsinvoice'),
(50, 'Can change items invoice', 13, 'change_itemsinvoice'),
(51, 'Can delete items invoice', 13, 'delete_itemsinvoice'),
(52, 'Can view items invoice', 13, 'view_itemsinvoice'),
(53, 'Can add payemet history', 14, 'add_payemethistory'),
(54, 'Can change payemet history', 14, 'change_payemethistory'),
(55, 'Can delete payemet history', 14, 'delete_payemethistory'),
(56, 'Can view payemet history', 14, 'view_payemethistory'),
(57, 'Can add items billing', 15, 'add_itemsbilling'),
(58, 'Can change items billing', 15, 'change_itemsbilling'),
(59, 'Can delete items billing', 15, 'delete_itemsbilling'),
(60, 'Can view items billing', 15, 'view_itemsbilling'),
(61, 'Can add invoices', 16, 'add_invoices'),
(62, 'Can change invoices', 16, 'change_invoices'),
(63, 'Can delete invoices', 16, 'delete_invoices'),
(64, 'Can view invoices', 16, 'view_invoices'),
(65, 'Can add billing', 17, 'add_billing'),
(66, 'Can change billing', 17, 'change_billing'),
(67, 'Can delete billing', 17, 'delete_billing'),
(68, 'Can view billing', 17, 'view_billing'),
(69, 'Can add type_of_voucher', 18, 'add_type_of_voucher'),
(70, 'Can change type_of_voucher', 18, 'change_type_of_voucher'),
(71, 'Can delete type_of_voucher', 18, 'delete_type_of_voucher'),
(72, 'Can view type_of_voucher', 18, 'view_type_of_voucher'),
(73, 'Can add table1', 19, 'add_table1'),
(74, 'Can change table1', 19, 'change_table1'),
(75, 'Can delete table1', 19, 'delete_table1'),
(76, 'Can view table1', 19, 'view_table1'),
(77, 'Can add table2', 20, 'add_table2'),
(78, 'Can change table2', 20, 'change_table2'),
(79, 'Can delete table2', 20, 'delete_table2'),
(80, 'Can view table2', 20, 'view_table2'),
(81, 'Can add sales_date', 21, 'add_sales_date'),
(82, 'Can change sales_date', 21, 'change_sales_date'),
(83, 'Can delete sales_date', 21, 'delete_sales_date'),
(84, 'Can view sales_date', 21, 'view_sales_date'),
(85, 'Can add sales', 22, 'add_sales'),
(86, 'Can change sales', 22, 'change_sales'),
(87, 'Can delete sales', 22, 'delete_sales'),
(88, 'Can view sales', 22, 'view_sales'),
(89, 'Can add items_relation', 23, 'add_items_relation'),
(90, 'Can change items_relation', 23, 'change_items_relation'),
(91, 'Can delete items_relation', 23, 'delete_items_relation'),
(92, 'Can view items_relation', 23, 'view_items_relation'),
(93, 'Can add history', 24, 'add_history'),
(94, 'Can change history', 24, 'change_history'),
(95, 'Can delete history', 24, 'delete_history'),
(96, 'Can view history', 24, 'view_history'),
(97, 'Can add purchase contracts', 25, 'add_purchasecontracts'),
(98, 'Can change purchase contracts', 25, 'change_purchasecontracts'),
(99, 'Can delete purchase contracts', 25, 'delete_purchasecontracts'),
(100, 'Can view purchase contracts', 25, 'view_purchasecontracts'),
(101, 'Can add purchase_ items_relation', 26, 'add_purchase_items_relation'),
(102, 'Can change purchase_ items_relation', 26, 'change_purchase_items_relation'),
(103, 'Can delete purchase_ items_relation', 26, 'delete_purchase_items_relation'),
(104, 'Can view purchase_ items_relation', 26, 'view_purchase_items_relation'),
(105, 'Can add purchase order', 27, 'add_purchaseorder'),
(106, 'Can change purchase order', 27, 'change_purchaseorder'),
(107, 'Can delete purchase order', 27, 'delete_purchaseorder'),
(108, 'Can view purchase order', 27, 'view_purchaseorder'),
(109, 'Can add purchase payemet history', 28, 'add_purchasepayemethistory'),
(110, 'Can change purchase payemet history', 28, 'change_purchasepayemethistory'),
(111, 'Can delete purchase payemet history', 28, 'delete_purchasepayemethistory'),
(112, 'Can view purchase payemet history', 28, 'view_purchasepayemethistory');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) COLLATE utf16_unicode_ci NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) COLLATE utf16_unicode_ci NOT NULL,
  `first_name` varchar(30) COLLATE utf16_unicode_ci NOT NULL,
  `last_name` varchar(150) COLLATE utf16_unicode_ci NOT NULL,
  `email` varchar(254) COLLATE utf16_unicode_ci NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf16 COLLATE=utf16_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf16 COLLATE=utf16_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf16 COLLATE=utf16_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext COLLATE utf16_unicode_ci,
  `object_repr` varchar(200) COLLATE utf16_unicode_ci NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL,
  `change_message` longtext COLLATE utf16_unicode_ci NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf16 COLLATE=utf16_unicode_ci;

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) COLLATE utf16_unicode_ci NOT NULL,
  `model` varchar(100) COLLATE utf16_unicode_ci NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf16 COLLATE=utf16_unicode_ci;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(2, 'auth', 'permission'),
(3, 'auth', 'group'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(6, 'sessions', 'session'),
(7, 'AiraPanel', 'categories'),
(8, 'AiraPanel', 'companies'),
(9, 'AiraPanel', 'subcategories'),
(10, 'AiraPanel', 'units'),
(11, 'AiraPanel', 'products'),
(12, 'AiraPanel', 'customers'),
(13, 'AiraPanel', 'itemsinvoice'),
(14, 'AiraPanel', 'payemethistory'),
(15, 'AiraPanel', 'itemsbilling'),
(16, 'AiraPanel', 'invoices'),
(17, 'AiraPanel', 'billing'),
(18, 'AiraPanel', 'type_of_voucher'),
(19, 'AiraPanel', 'table1'),
(20, 'AiraPanel', 'table2'),
(21, 'AiraPanel', 'sales_date'),
(22, 'AiraPanel', 'sales'),
(23, 'AiraPanel', 'items_relation'),
(24, 'AiraPanel', 'history'),
(25, 'AiraPanel', 'purchasecontracts'),
(26, 'AiraPanel', 'purchase_items_relation'),
(27, 'AiraPanel', 'purchaseorder'),
(28, 'AiraPanel', 'purchasepayemethistory');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL,
  `app` varchar(255) COLLATE utf16_unicode_ci NOT NULL,
  `name` varchar(255) COLLATE utf16_unicode_ci NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf16 COLLATE=utf16_unicode_ci;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'AiraPanel', '0001_initial', '2019-11-16 09:05:09.800072'),
(2, 'AiraPanel', '0002_auto_20191116_1435', '2019-11-16 09:05:11.838555'),
(3, 'contenttypes', '0001_initial', '2019-11-16 09:05:13.502355'),
(4, 'auth', '0001_initial', '2019-11-16 09:05:13.998611'),
(5, 'admin', '0001_initial', '2019-11-16 09:05:15.198162'),
(6, 'admin', '0002_logentry_remove_auto_add', '2019-11-16 09:05:15.448187'),
(7, 'admin', '0003_logentry_add_action_flag_choices', '2019-11-16 09:05:15.459161'),
(8, 'contenttypes', '0002_remove_content_type_name', '2019-11-16 09:05:15.594234'),
(9, 'auth', '0002_alter_permission_name_max_length', '2019-11-16 09:05:15.688988'),
(10, 'auth', '0003_alter_user_email_max_length', '2019-11-16 09:05:15.744069'),
(11, 'auth', '0004_alter_user_username_opts', '2019-11-16 09:05:15.754041'),
(12, 'auth', '0005_alter_user_last_login_null', '2019-11-16 09:05:15.817839'),
(13, 'auth', '0006_require_contenttypes_0002', '2019-11-16 09:05:15.821830'),
(14, 'auth', '0007_alter_validators_add_error_messages', '2019-11-16 09:05:15.832798'),
(15, 'auth', '0008_alter_user_username_max_length', '2019-11-16 09:05:15.888049'),
(16, 'auth', '0009_alter_user_last_name_max_length', '2019-11-16 09:05:15.946770'),
(17, 'auth', '0010_alter_group_name_max_length', '2019-11-16 09:05:16.000773'),
(18, 'auth', '0011_update_proxy_permissions', '2019-11-16 09:05:16.022715'),
(19, 'product', '0001_initial', '2019-11-16 09:05:16.608395'),
(20, 'product', '0002_auto_20191022_1604', '2019-11-16 09:05:17.908309'),
(21, 'sessions', '0001_initial', '2019-11-16 09:05:17.977027'),
(22, 'AiraPanel', '0003_auto_20191118_1228', '2019-11-18 06:58:55.163860'),
(23, 'AiraPanel', '0004_auto_20191122_1002', '2019-11-22 05:16:05.330181'),
(24, 'AiraPanel', '0005_auto_20191122_1005', '2019-11-22 05:16:05.850236'),
(25, 'AiraPanel', '0006_auto_20191122_1046', '2019-11-22 05:16:58.993763'),
(26, 'AiraPanel', '0007_auto_20191122_1051', '2019-11-22 05:21:28.308631'),
(27, 'AiraPanel', '0008_auto_20191122_1409', '2019-11-22 08:39:21.837465'),
(28, 'AiraPanel', '0009_invoices_status', '2019-11-22 11:31:54.214357'),
(29, 'AiraPanel', '0010_type_of_voucher', '2019-11-28 06:07:44.647606'),
(30, 'AiraPanel', '0011_auto_20191128_1252', '2019-11-28 07:23:00.399280'),
(31, 'AiraPanel', '0012_auto_20191130_1658', '2019-11-30 11:28:22.321433'),
(32, 'AiraPanel', '0013_auto_20191130_1804', '2019-11-30 12:34:31.233469'),
(33, 'AiraPanel', '0014_auto_20191130_1814', '2019-11-30 12:44:35.723780'),
(34, 'AiraPanel', '0015_auto_20191204_1038', '2019-12-04 05:08:55.972630'),
(35, 'AiraPanel', '0016_auto_20191204_1056', '2019-12-04 05:26:20.945626'),
(36, 'AiraPanel', '0017_auto_20191204_1120', '2019-12-04 05:50:20.560275'),
(37, 'AiraPanel', '0018_auto_20191207_1240', '2019-12-07 07:10:57.878455'),
(38, 'AiraPanel', '0019_invoices_type', '2019-12-07 10:14:47.054598'),
(39, 'AiraPanel', '0020_auto_20191211_1559', '2019-12-11 10:29:16.659226'),
(40, 'AiraPanel', '0021_auto_20191211_1604', '2019-12-11 10:34:32.489562'),
(41, 'AiraPanel', '0022_purchaseorder', '2019-12-13 12:01:54.842531'),
(42, 'AiraPanel', '0023_auto_20191219_1517', '2019-12-19 09:47:44.398640');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) COLLATE utf16_unicode_ci NOT NULL,
  `session_data` longtext COLLATE utf16_unicode_ci NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf16 COLLATE=utf16_unicode_ci;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `airapanel_billing`
--
ALTER TABLE `airapanel_billing`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `airapanel_billing_items`
--
ALTER TABLE `airapanel_billing_items`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `AiraPanel_billing_items_billing_id_itemsbilling_id_dc0414eb_uniq` (`billing_id`,`itemsbilling_id`),
  ADD KEY `AiraPanel_billing_items_billing_id_af8a0f7f` (`billing_id`),
  ADD KEY `AiraPanel_billing_items_itemsbilling_id_13d41225` (`itemsbilling_id`);

--
-- Indexes for table `airapanel_categories`
--
ALTER TABLE `airapanel_categories`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `airapanel_companies`
--
ALTER TABLE `airapanel_companies`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `airapanel_customers`
--
ALTER TABLE `airapanel_customers`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`),
  ADD UNIQUE KEY `aira_code` (`aira_code`);

--
-- Indexes for table `airapanel_history`
--
ALTER TABLE `airapanel_history`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `airapanel_invoices`
--
ALTER TABLE `airapanel_invoices`
  ADD PRIMARY KEY (`id`),
  ADD KEY `AiraPanel_invoices_company_id_f6c9a56e` (`company_id`),
  ADD KEY `AiraPanel_invoices_customer_id_fbf46056` (`customer_id`);

--
-- Indexes for table `airapanel_invoices_history`
--
ALTER TABLE `airapanel_invoices_history`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `AiraPanel_invoices_history_invoices_id_history_id_7be6cbd2_uniq` (`invoices_id`,`history_id`),
  ADD KEY `AiraPanel_invoices_history_invoices_id_33f789f2` (`invoices_id`),
  ADD KEY `AiraPanel_invoices_history_history_id_1106105f` (`history_id`);

--
-- Indexes for table `airapanel_invoices_items`
--
ALTER TABLE `airapanel_invoices_items`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `AiraPanel_invoices_items_invoices_id_itemsinvoice_99361c36_uniq` (`invoices_id`,`items_relation_id`),
  ADD KEY `AiraPanel_invoices_items_invoices_id_4b9b5a35` (`invoices_id`),
  ADD KEY `AiraPanel_invoices_items_itemsinvoice_id_d2b84dea` (`items_relation_id`);

--
-- Indexes for table `airapanel_invoices_payement_history`
--
ALTER TABLE `airapanel_invoices_payement_history`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `AiraPanel_invoices_payem_invoices_id_payemethisto_296108a6_uniq` (`invoices_id`,`payemethistory_id`),
  ADD KEY `AiraPanel_invoices_payement_history_invoices_id_92c46067` (`invoices_id`),
  ADD KEY `AiraPanel_invoices_payement_history_payemethistory_id_8be4c040` (`payemethistory_id`);

--
-- Indexes for table `airapanel_itemsbilling`
--
ALTER TABLE `airapanel_itemsbilling`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `airapanel_itemsbilling_company`
--
ALTER TABLE `airapanel_itemsbilling_company`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `AiraPanel_itemsbilling_c_itemsbilling_id_companie_8b874b2f_uniq` (`itemsbilling_id`,`companies_id`),
  ADD KEY `AiraPanel_itemsbilling_company_itemsbilling_id_e56386c2` (`itemsbilling_id`),
  ADD KEY `AiraPanel_itemsbilling_company_companies_id_1fe79284` (`companies_id`);

--
-- Indexes for table `airapanel_itemsbilling_customer`
--
ALTER TABLE `airapanel_itemsbilling_customer`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `AiraPanel_itemsbilling_c_itemsbilling_id_customer_5e4356ff_uniq` (`itemsbilling_id`,`customers_id`),
  ADD KEY `AiraPanel_itemsbilling_customer_itemsbilling_id_4ae781b4` (`itemsbilling_id`),
  ADD KEY `AiraPanel_itemsbilling_customer_customers_id_2297a22b` (`customers_id`);

--
-- Indexes for table `airapanel_items_relation`
--
ALTER TABLE `airapanel_items_relation`
  ADD PRIMARY KEY (`id`),
  ADD KEY `AiraPanel_items_relation_product_Id_id_c0f99a4a` (`product_Id_id`);

--
-- Indexes for table `airapanel_payemethistory`
--
ALTER TABLE `airapanel_payemethistory`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `airapanel_products`
--
ALTER TABLE `airapanel_products`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `pdt` (`pdt`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `airapanel_products_category`
--
ALTER TABLE `airapanel_products_category`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `AiraPanel_products_categ_products_id_categories_i_dee002df_uniq` (`products_id`,`categories_id`),
  ADD KEY `AiraPanel_products_category_products_id_5dce206c` (`products_id`),
  ADD KEY `AiraPanel_products_category_categories_id_58f855ea` (`categories_id`);

--
-- Indexes for table `airapanel_products_manufaturer`
--
ALTER TABLE `airapanel_products_manufaturer`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `AiraPanel_products_manuf_products_id_companies_id_3ba1c7f3_uniq` (`products_id`,`companies_id`),
  ADD KEY `AiraPanel_products_manufaturer_products_id_11eea24f` (`products_id`),
  ADD KEY `AiraPanel_products_manufaturer_companies_id_3533585b` (`companies_id`);

--
-- Indexes for table `airapanel_products_subcategory`
--
ALTER TABLE `airapanel_products_subcategory`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `AiraPanel_products_subca_products_id_subcategorie_62429067_uniq` (`products_id`,`subcategories_id`),
  ADD KEY `AiraPanel_products_subcategory_products_id_061fefb2` (`products_id`),
  ADD KEY `AiraPanel_products_subcategory_subcategories_id_36beb45a` (`subcategories_id`);

--
-- Indexes for table `airapanel_products_unit`
--
ALTER TABLE `airapanel_products_unit`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `AiraPanel_products_unit_products_id_units_id_c7963e7a_uniq` (`products_id`,`units_id`),
  ADD KEY `AiraPanel_products_unit_products_id_dc2b8e78` (`products_id`),
  ADD KEY `AiraPanel_products_unit_units_id_212468c2` (`units_id`);

--
-- Indexes for table `airapanel_purchasecontracts`
--
ALTER TABLE `airapanel_purchasecontracts`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `airapanel_purchasecontracts_items`
--
ALTER TABLE `airapanel_purchasecontracts_items`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `AiraPanel_purchasecontra_purchasecontracts_id_pur_b4de3860_uniq` (`purchasecontracts_id`,`purchase_items_relation_id`),
  ADD KEY `AiraPanel_purchasecontracts_items_purchasecontracts_id_6f68ae0b` (`purchasecontracts_id`),
  ADD KEY `AiraPanel_purchasecontracts_purchase_items_relation_id_5a49c156` (`purchase_items_relation_id`);

--
-- Indexes for table `airapanel_purchasecontracts_vendors`
--
ALTER TABLE `airapanel_purchasecontracts_vendors`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `AiraPanel_purchasecontra_purchasecontracts_id_cus_07ac2247_uniq` (`purchasecontracts_id`,`customers_id`),
  ADD KEY `AiraPanel_purchasecontracts_purchasecontracts_id_b6d83d2d` (`purchasecontracts_id`),
  ADD KEY `AiraPanel_purchasecontracts_vendors_customers_id_429ab823` (`customers_id`);

--
-- Indexes for table `airapanel_purchaseorder`
--
ALTER TABLE `airapanel_purchaseorder`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `airapanel_purchaseorder_items`
--
ALTER TABLE `airapanel_purchaseorder_items`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `AiraPanel_purchaseorder__purchaseorder_id_purchas_95c524b8_uniq` (`purchaseorder_id`,`purchase_items_relation_id`),
  ADD KEY `AiraPanel_purchaseorder_items_purchaseorder_id_36ef24f0` (`purchaseorder_id`),
  ADD KEY `AiraPanel_purchaseorder_ite_purchase_items_relation_id_613723d2` (`purchase_items_relation_id`);

--
-- Indexes for table `airapanel_purchaseorder_payement_history`
--
ALTER TABLE `airapanel_purchaseorder_payement_history`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `AiraPanel_purchaseorder__purchaseorder_id_purchas_b397c5f7_uniq` (`purchaseorder_id`,`purchasepayemethistory_id`),
  ADD KEY `AiraPanel_purchaseorder_pay_purchaseorder_id_8d7efc95` (`purchaseorder_id`),
  ADD KEY `AiraPanel_purchaseorder_pay_purchasepayemethistory_id_718953fa` (`purchasepayemethistory_id`);

--
-- Indexes for table `airapanel_purchaseorder_vendors`
--
ALTER TABLE `airapanel_purchaseorder_vendors`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `AiraPanel_purchaseorder__purchaseorder_id_custome_8a0270b1_uniq` (`purchaseorder_id`,`customers_id`),
  ADD KEY `AiraPanel_purchaseorder_vendors_purchaseorder_id_5b946076` (`purchaseorder_id`),
  ADD KEY `AiraPanel_purchaseorder_vendors_customers_id_bf8f6447` (`customers_id`);

--
-- Indexes for table `airapanel_purchasepayemethistory`
--
ALTER TABLE `airapanel_purchasepayemethistory`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `airapanel_purchase_items_relation`
--
ALTER TABLE `airapanel_purchase_items_relation`
  ADD PRIMARY KEY (`id`),
  ADD KEY `AiraPanel_purchase_items_relation_product_Id_id_4b4d7c5e` (`product_Id_id`);

--
-- Indexes for table `airapanel_sales`
--
ALTER TABLE `airapanel_sales`
  ADD PRIMARY KEY (`id`),
  ADD KEY `AiraPanel_sales_company_id_922e74e4` (`company_id`),
  ADD KEY `AiraPanel_sales_customer_id_ba4af8f7` (`customer_id`);

--
-- Indexes for table `airapanel_sales_history`
--
ALTER TABLE `airapanel_sales_history`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `AiraPanel_sales_date_sales_id_history_id_cf46cb8b_uniq` (`sales_id`,`history_id`),
  ADD KEY `AiraPanel_sales_date_sales_id_a2fd6c4b` (`sales_id`),
  ADD KEY `AiraPanel_sales_date_history_id_6a24912d` (`history_id`);

--
-- Indexes for table `airapanel_sales_items`
--
ALTER TABLE `airapanel_sales_items`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `AiraPanel_sales_items_sales_id_itemsinvoice_id_d01c3050_uniq` (`sales_id`,`items_relation_id`),
  ADD KEY `AiraPanel_sales_items_sales_id_7683c14e` (`sales_id`),
  ADD KEY `AiraPanel_sales_items_itemsinvoice_id_4f6ef94d` (`items_relation_id`);

--
-- Indexes for table `airapanel_subcategories`
--
ALTER TABLE `airapanel_subcategories`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `airapanel_units`
--
ALTER TABLE `airapanel_units`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissions_group_id_b120cbf9` (`group_id`),
  ADD KEY `auth_group_permissions_permission_id_84c5c92e` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  ADD KEY `auth_permission_content_type_id_2f476e4b` (`content_type_id`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_user_id_6a12ed8b` (`user_id`),
  ADD KEY `auth_user_groups_group_id_97559544` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permissions_user_id_a95ead1b` (`user_id`),
  ADD KEY `auth_user_user_permissions_permission_id_1fbb5f2c` (`permission_id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `airapanel_billing`
--
ALTER TABLE `airapanel_billing`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `airapanel_billing_items`
--
ALTER TABLE `airapanel_billing_items`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `airapanel_categories`
--
ALTER TABLE `airapanel_categories`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
--
-- AUTO_INCREMENT for table `airapanel_companies`
--
ALTER TABLE `airapanel_companies`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;
--
-- AUTO_INCREMENT for table `airapanel_customers`
--
ALTER TABLE `airapanel_customers`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;
--
-- AUTO_INCREMENT for table `airapanel_history`
--
ALTER TABLE `airapanel_history`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=86;
--
-- AUTO_INCREMENT for table `airapanel_invoices`
--
ALTER TABLE `airapanel_invoices`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=41;
--
-- AUTO_INCREMENT for table `airapanel_invoices_history`
--
ALTER TABLE `airapanel_invoices_history`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;
--
-- AUTO_INCREMENT for table `airapanel_invoices_items`
--
ALTER TABLE `airapanel_invoices_items`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=116;
--
-- AUTO_INCREMENT for table `airapanel_invoices_payement_history`
--
ALTER TABLE `airapanel_invoices_payement_history`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=33;
--
-- AUTO_INCREMENT for table `airapanel_itemsbilling`
--
ALTER TABLE `airapanel_itemsbilling`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `airapanel_itemsbilling_company`
--
ALTER TABLE `airapanel_itemsbilling_company`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `airapanel_itemsbilling_customer`
--
ALTER TABLE `airapanel_itemsbilling_customer`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `airapanel_items_relation`
--
ALTER TABLE `airapanel_items_relation`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=229;
--
-- AUTO_INCREMENT for table `airapanel_payemethistory`
--
ALTER TABLE `airapanel_payemethistory`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=34;
--
-- AUTO_INCREMENT for table `airapanel_products`
--
ALTER TABLE `airapanel_products`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
--
-- AUTO_INCREMENT for table `airapanel_products_category`
--
ALTER TABLE `airapanel_products_category`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
--
-- AUTO_INCREMENT for table `airapanel_products_manufaturer`
--
ALTER TABLE `airapanel_products_manufaturer`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
--
-- AUTO_INCREMENT for table `airapanel_products_subcategory`
--
ALTER TABLE `airapanel_products_subcategory`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
--
-- AUTO_INCREMENT for table `airapanel_products_unit`
--
ALTER TABLE `airapanel_products_unit`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
--
-- AUTO_INCREMENT for table `airapanel_purchasecontracts`
--
ALTER TABLE `airapanel_purchasecontracts`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=64;
--
-- AUTO_INCREMENT for table `airapanel_purchasecontracts_items`
--
ALTER TABLE `airapanel_purchasecontracts_items`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=52;
--
-- AUTO_INCREMENT for table `airapanel_purchasecontracts_vendors`
--
ALTER TABLE `airapanel_purchasecontracts_vendors`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=107;
--
-- AUTO_INCREMENT for table `airapanel_purchaseorder`
--
ALTER TABLE `airapanel_purchaseorder`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;
--
-- AUTO_INCREMENT for table `airapanel_purchaseorder_items`
--
ALTER TABLE `airapanel_purchaseorder_items`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;
--
-- AUTO_INCREMENT for table `airapanel_purchaseorder_payement_history`
--
ALTER TABLE `airapanel_purchaseorder_payement_history`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
--
-- AUTO_INCREMENT for table `airapanel_purchaseorder_vendors`
--
ALTER TABLE `airapanel_purchaseorder_vendors`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
--
-- AUTO_INCREMENT for table `airapanel_purchasepayemethistory`
--
ALTER TABLE `airapanel_purchasepayemethistory`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
--
-- AUTO_INCREMENT for table `airapanel_purchase_items_relation`
--
ALTER TABLE `airapanel_purchase_items_relation`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=229;
--
-- AUTO_INCREMENT for table `airapanel_sales`
--
ALTER TABLE `airapanel_sales`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=66;
--
-- AUTO_INCREMENT for table `airapanel_sales_history`
--
ALTER TABLE `airapanel_sales_history`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=66;
--
-- AUTO_INCREMENT for table `airapanel_sales_items`
--
ALTER TABLE `airapanel_sales_items`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=178;
--
-- AUTO_INCREMENT for table `airapanel_subcategories`
--
ALTER TABLE `airapanel_subcategories`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
--
-- AUTO_INCREMENT for table `airapanel_units`
--
ALTER TABLE `airapanel_units`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=113;
--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=29;
--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=43;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
