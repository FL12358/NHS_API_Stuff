from requests import get
import matplotlib.pylab as plt

def get_data(url):
    response = get(endpoint, timeout=10)
    
    if response.status_code >= 400:
        raise RuntimeError(f'Request failed: { response.text }')
        
    return response.json()
    

if __name__ == '__main__':
    endpoint = (
        'https://api.coronavirus.data.gov.uk/v1/data?'
        'filters=areaType=ltla;areaName=Test Valley&'
        'structure={"date":"date","newCases":"newCasesByPublishDate"}'
    )
    
    data = get_data(endpoint)
    print(data)

    date = []
    cases = []

    for i in data["data"]:
        #print(i)
        date.append(i.get("date"))
        cases.append(i.get("newCases"))


    fig = plt.figure()
    ax = fig.gca()
    ax.bar(date,cases)
    ax.set_xlim('2020-01-02','2020-11-07')
    ax.set_ylim(0,40)
    ax.xaxis.set_tick_params(length=0, rotation=45)
    temp = ax.xaxis.get_ticklabels()
    temp = list(set(temp) - set(temp[::30]))
    for i in temp:
        i.set_visible(False)
        
    plt.tight_layout()


    plt.title("Corona cases")
    plt.savefig("ronaCases.png", dpi=300)
