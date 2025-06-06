import plotly.express as px

def you_location_map() -> None:
    """
    reference: https://x.com/clcoding/status/1930807083840270651
    """
    country = input("Enter the country name: ")
    data = {
        'Country': [country],
        'Values': [100]}
    fig = px.choropleth(
        data,
        locations='Country',
        locationmode='country names',
        color='Values',
        color_continuous_scale='Inferno',
        title=f'Country Map Highlighting {country}')
    fig.show()
    # source code --> clcoding.com

def test():
    x = False
    y = True
    z = False
    print(not x and (y or z and not y))

def is_even(number):
    if number % 2:
        return True
        return False

if __name__ == '__main__':
    # you_location_map()
    # test()
    print(is_even(2))