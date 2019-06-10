# Usage

In Terminal or CMD, navigate to the main Scrapy project folder, and run one of the spiders:

### Creating Scrapy Craigslist Spider
```
$ cd Desktop/Scrapy/

$ scrapy startproject craigslist

$ cd craigslist

$ scrapy genspider jobs newyork.craigslist.org
```

### Craigslist Scrapy Spider #1 - Titles

```
$ scrapy shell 'https://newyork.craigslist.org/d/activity-partners/search/egr'

# check the status
In [1]: response.status                                
Out[1]: 200

In [4]: response.xpath('//a[@class="result-title hdrlnk"]/text()').extract()                                                                     
Out[4]:
['Facade / Building Envelope Architect',
 'Asst. Estimator/Project Manager',
 'ARCHITECTURAL DESIGNER / DRAFTS PERSON',
 'Architect',
 'Architecture Intern',
 'INTERMEDIATE ARCHITECT / JOB CAPTAIN',
 'Construction Assistant PM / Superintendent',
 'Design Intern at European Home Design Firm -summer/part time',
 'Construction Inspector (Water Main)',
 'ARCHITECT (New York City)',
 'Construction Inspector / Special Inspector',
 'Architectural Designer',
 'Structural Engineer',
 'ARCHITECTURAL METAL DRAFTER',
 'Construction Project Manager',
 'Architectural draftsperson needed',
 'Special Inspector (Concrete)',
 'Facade / Building Envelope Architect',
 'DOT/ DOB Permit expediter',
 'Business Development Leader',
 'Hotel Engineer wanted!',
 'Manager Needed for Small Busy Commercial Construction Firm',
 'Maintenance Manger',
 'Expediting C of O coordinator',
 'GOSHOW ARCHITECTS IS HIRING: INTERN ARCHITECT I: ENTRY LEVEL JUNIOR',
 'Construction Project Manager',
 'Interior Designer',
 'Maintenance Engineer',
 'Architectural Intern',
 'CONSTRUCTION PROJECT MANAGER/ ESTIMATOR',
 'Construction Manager',
 'Junior Interior Designer',
 'Project Engineer',
 'Project Engineer position',
 'High-End Residential Architect',
 'Class 1 or 2 Expeditor',
 'Intern - Architectural / Construction Mngmnt',
 'Junior Draftsman needed for part time work',
 'NYC DOB Class 1 or 2 Filing Representative',
 'Intern in M.E.P. Engineering',
 'Interior Architectural Associate with Exceptional REVIT Experience',
 'Junior/Intermediate Architect',
 'Drafting/Estimating Internship',
 'EXPERIENCED ARCHITECT/ DRAFTER',
 'Residential Construction Project Manager - Townhouse/Luxury High End',
 'ESTIMATOR - DRYWALL & CEILINGS',
 'Mechanical Designers',
 'Field Super, Project Coord, & Admin',
 'EXPERIENCED ARCHITECT',
 'NYC Architecture Firm seeking AutoCad Draftsman',
 'HealthCare Architect',
 'Architectural Metal Cost Estimator',
 'Document Reviewer',
 'Architectural Designer',
 'Goshow Architects seeks Project Managers to join our team in New York',
 'Goshow Architects seeks Project Architects to join our team in New Yor',
 'Project Architect - 1 to 5 yrs exp',
 'Construction Inspector - Civil/Structural',
 'AudoCad Drafter',
 'Project Coordinator / Intermediate Architect',
 'AV/ IT Design Engineer',
 'Mechanical Engineer',
 'Plumbing/Fire Protection Engineer',
 'PE/SE (STRUCTURAL)',
 'Survey party Chief, Instrument Person, Rod Man',
 'Junior-Intermediate Interior Designer',
 'Estimator',
 'PROJECT MANAGER',
 'Junior Estimator (L.I.C)',
 'Product designer Industrial developer for fitness product',
 'CAD Designer',
 'AutoCad Draftperson and Assistant Architect',
 'Architectural Draftsperson',
 'Construction Site Safety Manager',
 'Environmental Field Technician',
 'Environmental Project Manager - Mid Level',
 'Environmental Project Manager - Senior Level',
 'Drafter wanted : Greenpoint, Brooklyn',
 'Junior Interior Designer / Assistant',
 'Construction Inspector - Civil/Structural',
 'Cad Drafter - Architectural/Engineering background',
 'Construction Clerk/Project Manager M/F',
 'JR project manager/Misc Steel draft person apprentice with experience',
 'Landscape Designer (2-3 years Experience)',
 'Senior Landscape Designer/Architect',
 'Intermediate Designer',
 'Land Surveyor Assistant/Helper ASAP',
 'Looking for Architect / DOB Expert',
 'Autocad Drafter',
 'Professional wanted',
 'Structural Engineer/Architect/CAD Operator',
 'Residential Interior Designer+Project Manager',
 'Architect / Drafter',
 'Drafting / Millwork Technical Assistant for modern showroom/firm',
 'Construction Health & Safety Assistant',
 'Construction Estimator/Project Manager',
 'CAD Draftsman/Estimator',
 'EXPERIENCED NYC DEPARTMENT OF BUILDINGS (DOB) FILING REPRESENTATIVE',
 'Architectural Intern / Administrative assistant',
 'Guaranteed $180,000 Salary',
 'Architectural Field Representative',
 'architectural autoCAD draftsman',
 'Quality Engineer - Experience in FDA',
 'Project Architect - Interiors',
 'Construction Project Manager',
 'AutoCAD Drafter (Brooklyn, NY)',
 'Project Coordinator',
 'Construction Engineer / Project Manager',
 'Surveyor /Cad Drafter',
 'Maintenance Engineer',
 'CAD / Revit BIM Specialist / Trainer',
 'Bridge Inspection - Team Leader',
 'Bridge Inspection - Assistant Team Leader',
 'Bridge Inspection - Assistant Team Leader',
 'Bridge Inspection - Team Leader',
 'Draftsperson/Designer',
 'Architectural Project Manager',
 'Freelance INTERMEDIATE Architects (REVIT)',
 'Survey CAD Technician',
 'Survey Crew Chief']

```


```
$ scrapy crawl jobs -s DOWNLOAD_DELAY=3
```
