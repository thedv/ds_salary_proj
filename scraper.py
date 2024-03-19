#!/usr/bin/env python
# coding: utf-8

# In[18]:


from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium import webdriver
import time
import pandas as pd
from selenium.webdriver.common.by import By


# In[55]:


def get_jobs(keyword, num_jobs, verbose, path, slp_time):
    
    '''Gathers jobs as a dataframe, scraped from Glassdoor'''
    
    #Initializing the webdriver
    options = webdriver.ChromeOptions()
    
    #Uncomment the line below if you'd like to scrape without a new Chrome window every time.
    #options.add_argument('headless')
    #Let the page load. Change this number based on your internet speed.
    #Or, wait until the webpage is loaded, instead of hardcoding it.
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(executable_path=path, options=options)
    driver.set_window_size(1120, 1000)
    
    url = "https://www.glassdoor.com/Job/jobs.htm?suggestCount=0&suggestChosen=false&clickSource=searchBtn&typedKeyword="+keyword+"&sc.keyword="+keyword+"&locT=&locId=&jobType="
    #url = 'https://www.glassdoor.com/Job/deel-jobs-SRCH_KO0,4.htm'
    #url = 'https://www.glassdoor.com/Job/jobs.htm?sc.keyword="' + keyword + '"&locT=C&locId=1147401&locKeyword=San%20Francisco,%20CA&jobType=all&fromAge=-1&minSalary=0&includeNoSalaryJobs=true&radius=100&cityId=-1&minRating=0.0&industryId=-1&sgocId=-1&seniorityType=all&companyId=-1&employerSizes=0&applicationType=0&remoteWorkType=0'
    driver.get(url)
    
    time.sleep(slp_time)

    try:
        for _ in range(33):  # Click the button 100 times
            load_more_button = driver.find_element_by_xpath("//button[@data-test='load-more']")
            load_more_button.click()
            time.sleep(4)  # Wait for more jobs to load
    except NoSuchElementException:
        print("No 'Show more jobs' button found.")
    '''
    try:
        driver.find_element_by_xpath('.//buton[@class="button_Button__MlD2g button-base_Button__knLaX"]').click()
    except NoSuchElementException:
        print("Scraping terminated before reaching target number of jobs. Needed {}, got {}.".format(num_jobs, len(jobs)))
    '''    
    print('Started')
    jobs = []

    while len(jobs) < num_jobs:  #If true, should be still looking for new jobs.



         
        #Going through each job in this page
        #job_buttons = driver.find_elements(By.CSS_SELECTOR,"li[class^='JobsList_jobListItem']")  #jl for Job Listing. These are the buttons we're going to click.
        job_buttons = driver.find_elements(By.CSS_SELECTOR,"li[class^='JobsList_jobListItem']")
        print(len(job_buttons))
        for job_button in job_buttons: 

            print("Progress: {}".format("" + str(len(jobs)) + "/" + str(num_jobs)))

            if len(jobs) >= num_jobs:
                break
           

            job_button.click()  #You might 
            time.sleep(1)
            collected_successfully = False


          
            while not collected_successfully:
                try:
                    company_name = job_button.find_element_by_xpath('.//span[@class="EmployerProfile_compactEmployerName__LE242"]').text
                    location = job_button.find_element_by_xpath('.//div[@class="JobCard_location__rCz3x"]').text
                    job_title = job_button.find_element_by_xpath('.//a[contains(@class, "JobCard_jobTitle___7I6y")]').text
                    print(company_name)
                    try: 
                        driver.find_element_by_xpath(".//button[@class='JobDetails_showMore___Le6L']").click()
                    except:
                        print('Show button not foud')
                    time.sleep(1)

                    job_description = driver.find_element(By.XPATH, './/div[@class="JobDetails_jobDescription__uW_fK JobDetails_showHidden__C_FOA"]').text
                    collected_successfully = True

                except:

                    time.sleep(2)

            try:
                salary_estimate = job_button.find_element_by_xpath('.//div[@class="JobCard_salaryEstimate__arV5J"]').text
            except NoSuchElementException:
                salary_estimate = -1 #You need to set a "not found value. It's important."
            
            try:
                rating = job_button.find_element_by_xpath('.//div[@class="EmployerProfile_ratingContainer__ul0Ef"]').text
            except NoSuchElementException:
                rating = -1 #You need to set a "not found value. It's important."
            


            #Printing for debugging
            if verbose:
                print("Job Title: {}".format(job_title))
                print("Salary Estimate: {}".format(salary_estimate))
                print("Job Description: {}".format(job_description[:500]))
                print("Rating: {}".format(rating))
                print("Company Name: {}".format(company_name))
                print("Location: {}".format(location))
                
            


            #Going to the Company tab...
            #clicking on this:
            #<div class="tab" data-tab-type="overview"><span>Company</span></div>
            #try:
                #driver.find_element_by_xpath('.//div[@class="tab" and @data-tab-type="overview"]').click()
                

            try:
                size = driver.find_element(By.XPATH, "//div[@class='JobDetails_overviewItem__cAsry']//span[@class='JobDetails_overviewItemLabel__KjFln' and text()='Size']/following-sibling::div[@class='JobDetails_overviewItemValue__xn8EF']").text
            except NoSuchElementException:
                size = -1

            try:
                founded = driver.find_element(By.XPATH, "//div[@class='JobDetails_overviewItem__cAsry']//span[@class='JobDetails_overviewItemLabel__KjFln' and text()='Founded']/following-sibling::div[@class='JobDetails_overviewItemValue__xn8EF']").text
            except NoSuchElementException:
                founded = -1

            try:
                type_of_ownership = driver.find_element(By.XPATH, "//div[@class='JobDetails_overviewItem__cAsry']//span[@class='JobDetails_overviewItemLabel__KjFln' and text()='Type']/following-sibling::div[@class='JobDetails_overviewItemValue__xn8EF']").text
            except NoSuchElementException:
                type_of_ownership = -1

            try:
                industry = driver.find_element(By.XPATH, "//div[@class='JobDetails_overviewItem__cAsry']//span[@class='JobDetails_overviewItemLabel__KjFln' and text()='Industry']/following-sibling::div[@class='JobDetails_overviewItemValue__xn8EF']").text
            except NoSuchElementException:
                industry = -1

            try:
                sector = driver.find_element(By.XPATH, "//div[@class='JobDetails_overviewItem__cAsry']//span[@class='JobDetails_overviewItemLabel__KjFln' and text()='Sector']/following-sibling::div[@class='JobDetails_overviewItemValue__xn8EF']").text
            except NoSuchElementException:
                sector = -1

            try:
                revenue = driver.find_element(By.XPATH, "//div[@class='JobDetails_overviewItem__cAsry']//span[@class='JobDetails_overviewItemLabel__KjFln' and text()='Revenue']/following-sibling::div[@class='JobDetails_overviewItemValue__xn8EF']").text
            except NoSuchElementException:
                revenue = -1


            '''
            except NoSuchElementException:  #Rarely, some job postings do not have the "Company" tab.
                size = -1
                founded = -1
                type_of_ownership = -1
                industry = -1
                sector = -1
                revenue = -1

            '''
                
            if verbose:
                print("Size: {}".format(size))
                print("Founded: {}".format(founded))
                print("Type of Ownership: {}".format(type_of_ownership))
                print("Industry: {}".format(industry))
                print("Sector: {}".format(sector))
                print("Revenue: {}".format(revenue))
                print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
         
            jobs.append({"Job Title" : job_title,
            "Salary Estimate" : salary_estimate,
            "Job Description" : job_description,
            "Rating" : rating,
            "Company Name" : company_name,
            "Location" : location,
            "Size" : size,
            "Founded" : founded,
            "Type of ownership" : type_of_ownership,
            "Industry" : industry,
            "Sector" : sector,
            "Revenue" : revenue})
            


            #add job to jobs
             
                 
        #Clicking on the "next page" button
        
        
    return pd.DataFrame(jobs)  #This line converts the dictionary object into a pandas DataFrame.

