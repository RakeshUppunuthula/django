
from django import forms
from .models import review

# class ReviewForm(forms.Form):
#     user_Name = forms.CharField(
#         label="Your Name",
#         max_length=100,
#         error_messages={
#             "required": "the name should be entered",
#             "max_length": "the value is must not be greater than 100",
#         },
#     )

#     review_text =forms.CharField(label="Your Feedback", widget=forms.Textarea ,max_length=200)
#     rating=forms.IntegerField(label="your rating",min_value=1,max_value=5)


class ReviewForm(forms.ModelForm):
    class Meta:
        model = review
        fields= '__all__'
        labels={ 
             "user_Name" : "Your Name",
             "rating":"Your Rating",
             "review_Text":" Review Text"
        }
        error_messages={

           "user_Name":{
               "required":"the data must be entered",
               "max_length":"the maximum lem=ngth should be 100"

           }
        }


      