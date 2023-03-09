Technologies
* ETL Tool - pentaho
* Database - PostgreSQL
* Reporting - Power BI

Business Intelligence

    Set of *processes*, know-how, aplications and technologies.
    It enables to optimize processes, gather overview of business situation.
    It gives the business and edge over competition.

It's not about technologies.

Technology changes, the basic principle stays.
* Company collect data, if it can leverage them, it gives it an edge.
    * e.g. I know when you run out of a product, I send you a promo-code so you buys it again.


Data Warehouse Examples
* Books
* SQL Database
* Excel sheets
* SQL Code

Data Warehouse
* consistency and reliability.
* Often implemented as as big database.
* Often uses complicated code for measuring KPIs.
* Itself it is a project, someone must develop and maintain it.
* When done right, the information is transparent and auditable.

## Case Study

Company XYZ
* new systems: ERP, CRM, SCM

Digitalization

Problems:
* Reporting - slow and dumb
* Data are not consolidated
* Product information are divergent
* It requires a lot of manual work

BSEARCH (SVYHLEDAT) - returns

Power Query
Power BI

### Data Integration
* Joining data tables

Data warehouse should model the business logic.
It transforms multiple data sources.

Excel has data connectors.
On update it reloads the data.

The raw data should never be in simple file e.g. Excel sheet, so the leaks are harder to do.


Business Definitions must be clear and transparent, so every entity agrees when calculated.

### Reporting

To whom the report is made:
* user - sees details related to his field
* analytic - sees more information except the critically confidential
* manager - confindential information about fields he has responsibility
* controlling - excel with details
* director - very simple reports over all domains


Customer pathway (experience)
* How the customer behaves on the website / in life.
* Customer Experience 360 - segmentation


Company evaluation based on data.

### Prediction Models

* When the new technology pays off.
* When a specific machine breaks.
* Cluster analysis


## Stories

Wallmart
* pregnant woman is ultra loyal

Barack Obama
* won the presidential thanks to better analytics of unified people behaviour.
* ->

* EDW as a Source of Information

## History

1. Until 15. century
    * Master - student
    * Could create anything
2. 15.-16. century north Italy
    * Manufacture
    * This requires some system to organize the information
    * Employees were less skilled, doing less simple job
3. Scientific Management Theory - Winslow Taylor
    * the smaller individual parts, the better and cheaper it become
4. Henry Ford
    * motivated employees
    * automated production line
5. Tomas Bata
    * Combination of Taylor and Ford
6. 1970 Edgar Frank Codd from IBM - A Relational Model of Data for Large Shared Data Banks
7. BI 1.0 - Tools using database
    * These are the ones who created it Oracle, IBM, Microsoft, Teradata, SAP
    * business intelligence was for the big players
8. BI 2.0 - Internet
    * business intelligence for smaller shops
9. Cloud
    * Everything is tracked, ...
    * Business Intelligence became critical for the business.


## Database Model

* Conceptual model
    * Relations between entities
* Logical (database) model
    * Maps conceptual model to database tables
    * Normalization CNF
* Physical model
    * Specific implementation of logical model
    * e.g. data segmentation, indexes, partitioning

## Data Warehouse (DWH) Architecture

* Source layer - inputs e.g. sap, excel
* Landing layer e.g. file system, or ETL (extract, transform, load)
* Database
    * Staging layer - raw data in database
    * Integrated layer (IDL) / target - clean, normalized data, consolidation
    * Access Layer - prepared data for special purposes, aggregations etc.
* Information delivery layer

## Integrated Data Layer Modeling

* It should model the underlying business, not fit the collected data.

## Definitions

* TOGAF - The Open Group Architecture Framework
* KPI - Key Performance Indicator
* CRM - Customer Relationship Management
* ERP - Enterprise Resource Planning
* SCM - Supply Chain Management
* EDW - Enterprise Data Warehouse
* ETL - Extract, transform, load
* OLAP - Online analytical, processing

### Term Project

1. You got data and business questions
2. Reporting
3. Answer the business questions

### First Part

* Logical database model
* Database PostgreSQL
