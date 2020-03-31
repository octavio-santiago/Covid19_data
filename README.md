# Covid19_data
Data about the Covid-19 around the world and some detailed data from Brazil.
Images with some analysis.
Codes from simulations.

## Databases 

Database from John Hopkins -  https://github.com/CSSEGISandData/COVID-19 

https://systems.jhu.edu/research/public-health/ncov/ 

 

Coronavirus no Brasil - https://g1.globo.com/ciencia-e-saude/noticia/2020/03/12/sociedade-brasileira-de-infectologia-divulga-informacoes-sobre-coronavirus-leia.ghtml 

https://www.nytimes.com/2020/02/18/opinion/coronavirus-china-numbers.html 

 

## The SIR Model 

https://www.maa.org/press/periodicals/loci/joma/the-sir-model-for-spread-of-disease-the-differential-equation-model 

S = S(t), is the number of susceptible individuals, 

I = I(t), is the number of infected individuals, and 

R = R(t), is the number of recovered individuals. 

### Parameters 

Study from Imperial College - UK 
https://www.imperial.ac.uk/media/imperial-college/medicine/sph/ide/gida-fellowships/Imperial-College-COVID19-NPI-modelling-16-03-2020.pdf 

Whilst our understanding of infectious diseases and their prevention is now very different compared to in 1918, most of the countries across the world face the same challenge today with COVID-19, a virus with comparable lethality to H1N1 influenza in 1918. Two fundamental strategies are possible2 :  

(a) Suppression. Here the aim is to reduce the reproduction number (the average number of secondary cases each case generates), R, to below 1 and hence to reduce case numbers to low levels or (as for SARS or Ebola) eliminate human-to-human transmission. The main challenge of this approach is that NPIs (and drugs, if available) need to be maintained – at least intermittently - for as long as the virus is circulating in the human population, or until a vaccine becomes available. In the case of COVID-19, it will be at least a 12-18 months before a vaccine is available3 . Furthermore, there is no guarantee that initial vaccines will have high efficacy.  

(b) Mitigation. Here the aim is to use NPIs (and vaccines or drugs, if available) not to interrupt transmission completely, but to reduce the health impact of an epidemic, akin to the strategy adopted by some US cities in 1918, and by the world more generally in the 1957, 1968 and 2009 influenza pandemics. In the 2009 pandemic, for instance, early supplies of vaccine were targeted at individuals with pre-existing medical conditions which put them at risk of more severe disease4 . In this scenario, population immunity builds up through the epidemic, leading to an eventual rapid decline in case numbers and transmission dropping to low levels.  

The strategies differ in whether they aim to reduce the reproduction number, R, to below 1 (suppression) – and thus cause case numbers to decline – or to merely slow spread by reducing R, but not to below 1. 
 

Based on fits to the early growth-rate of the epidemic in Wuhan, we make a baseline assumption that R0=2.4 but examine values between 2.0 and 2.6. 

The age-stratified proportion of infections that require hospitalisation and the infection fatality ratio (IFR) were obtained from an analysis of a subset of cases from China12 . These estimates were corrected for non-uniform attack rates by age and when applied to the GB population result in an IFR of 0.9% with 4.4% of infections hospitalised (Table 1). We assume that 30% of those that are hospitalised will require critical care (invasive mechanical ventilation or ECMO) based on early reports from COVID-19 cases in the UK, China and Italy (Professor Nicholas Hart, personal communication). Based on expert clinical opinion, we assume that 50% of those in critical care will die and an age-dependent proportion of those that do not require critical care die (calculated to match the overall IFR). We calculate bed demand numbers assuming a total duration of stay in hospital of 8 days if critical care is not required and 16 days (with 10 days in ICU) if critical care is required. With 30% of hospitalised cases requiring critical care, we obtain an overall mean duration of hospitalisation of 10.4 days, slightly shorter than the duration from hospital admission to discharge observed for COVID-19 cases internationally13 (who will have remained in hospital longer to ensure negative tests at discharge) but in line with estimates for general pneumonia admissions 

 

## Leitos no brasil 

http://tabnet.datasus.gov.br/cgi/tabcgi.exe?cnes/cnv/leiintbr.def 

 

## Assumptions 

We are assuming that the country can test and report only 10% of real cases. 

The day 1 is when the country reaches 100 confirmed cases. 

 

## Log Model 

Since the number of confirmed cases follow an exponential distribution we can use a log-linear model to predict new cases. The real cases can be modeled as C=a exp (kt) and the log(10) scale:  log(C)=log(a) + kt 

Using a linear regression (ax + b) on the Log(10) scaled confirmed cases we can find good results if the infection rate not vary, however if the rate changes the model begins to fail and the error rises along the time. As we can see below, the linear regression for Brazil gives us a R square of 0,977 and a MAE of 343. The model with parameters is y = 0,128 x + 0,537 

When the rate varies the curve begins to follow a polynomial distribution and we can model using (a x^2 + bx + c). Modeling a Log curve with a polynomial equation gives us a R square of 0,99 and a MAE of 58, that is a much better fit than the Linear model. 


## Analyzing Deaths 

USA population is 327 milion and Brazil population is 210 milion, so is reasonable to compare these countries.  

Variation of death rate per day 

 

Death rate per infected  

 

## Update from 28/03/2020 

### Brazil 

The peak will be within:  39 days – 6/5/2020 


Real confirmed cases x Predicted - Benchmark 

 

Infected curve evolution with time 

Adjusting the curve every two days since the first 5 days.  

The blue curve is the most recent. 

The red curves are the past curves. 

 

 

### USA 

The peak will be within:  25 days – 22/4/2020 


Which matches with the US Centers for Disease Control and Prevention estimation. 

https://edition.cnn.com/2020/03/25/health/coronavirus-death-peak-three-weeks-epidemiologist/index.html 


 

Real confirmed cases x Predicted - Benchmark 

 

 

 

Infected curve evolution with time 

Adjusting the curve every two days since the first 5 days.  

The blue curve is the most recent. 

The red curves are the past curves. 

 

 
