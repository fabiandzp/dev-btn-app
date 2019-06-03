from behave import *
from selenium import webdriver

##from code.tests.acceptance.page_model.blog_page import BlogPage
#from code.tests.acceptance.page_model.home_page import HomePage

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('headless')

use_step_matcher('re') #maps the steps to diferents variables

@given('I am on the homepage')
def step_impl(context):
    # Se crea la propiedad browser en la variable contexto
    #context.driver = webdriver.Chrome(chrome_options=chrome_options)  # It will look in the web driver in the path
    context.driver = webdriver.Chrome() # It will look in the web driver in the path
    context.driver.get('http://127.0.0.1:5000')


    #page = HomePage(context.driver)
    #context.driver.get(page.url)

@given('I am on the blog page')
def step_impl(context):
    # Se crea la propiedad browser en la variable contexto
    #context.driver = webdriver.Chrome() # It will look in the web driver in the path
    context.driver = webdriver.Chrome(chrome_options=chrome_options)

    context.driver.get('http://127.0.0.1:5000/blog')
    #page = BlogPage(context.driver)
    #context.driver.get(page.url)


@then('I am on the blog page')
def step_impl(context): #Context property, se pueden almacenar valores en esa propiedad si se requiere
    expected_url = 'http://127.0.0.1:5000/blog'
    #expected_url = BlogPage(context.driver).url
    assert context.driver.current_url == expected_url #Usamos python assert by default


@then('I am on the homepage')
def step_impl(context): #Context property, se pueden almacenar valores en esa propiedad si se requiere
    expected_url = 'http://127.0.0.1:5000/'
    #expected_url = HomePage(context.driver).url
    assert context.driver.current_url == expected_url #Usamos python assert by default