from io import BytesIO 
import base64
import matplotlib.pyplot as plt

def get_graph():
   buffer = BytesIO()         

   plt.savefig(buffer, format='png')

   buffer.seek(0)

   image_png=buffer.getvalue()

   graph=base64.b64encode(image_png)

   graph=graph.decode('utf-8')

   buffer.close()

   return graph

def get_chart(chart_type, data, **kwargs):
   plt.switch_backend('AGG')

   fig=plt.figure(figsize=(6,3))

   if chart_type == '#1':
        diffs = ['easy','medium','hard','intermediate']
        num_diffs = []
        for diff in diffs:
            num_diffs.append(data['difficulty'].value_counts().get(diff,0))
        plt.xlabel("Difficulty")
        plt.ylabel("# of Recipes")
        plt.bar(diffs, num_diffs)

   elif chart_type == '#2':
       labels=kwargs.get('labels')
       diffs = ['easy','medium','hard','intermediate']
       num_diffs = []
       for diff in diffs:
            num_diffs.append(data['difficulty'].value_counts().get(diff,0))
            print(num_diffs)

       percent_diffs = [ x / data.index.size for x in num_diffs] 
       plt.xlabel("% of Recipes by Difficulty")
       plt.pie(percent_diffs, labels=labels)

   elif chart_type == '#3':
        times = data['cooking_time'].unique()
        print(data['cooking_time'].unique())
        num_times = []
        for time in times:
            num_times.append(data['cooking_time'].value_counts().get(time,0))
        plt.xlabel("Cooking Time (min)")
        plt.ylabel("# of Recipes")
        plt.plot(times, num_times)
   else:
       print ('unknown chart type')

   plt.tight_layout()

   chart =get_graph() 
   return chart   
    
def make_clickable_both(val):
    name, url = val.split('#')
    return f'<a href="{url}">{name}</a>'  

def make_image(val):
    return f'<img width= "100px" height= "100px" src="/media/{val}" />'

