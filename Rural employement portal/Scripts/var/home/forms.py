from django import forms
from . models1 import pub
from . models2 import panchayath
from . models3 import ads
from . models4 import workemployee
from . models5 import workrequest
from . models6 import notifition
from . models8 import entry12
from . models9 import workcomplete
from . models10 import complaints
from . models12 import reply2
from . models13 import user
from . models14 import empattendence
from . models15 import newwork
from . models16 import feedbacks
from . models18 import salary
from . models19 import message1
import re
from django.core.exceptions import ValidationError
from . models20 import reply12
from datetime import datetime

KERALA_DISTRICTS = (
    ('SELECT DISTRICT','SELECT DISTRICT') ,
    ('Alappuzha', 'Alappuzha'),
    ('Ernakulam', 'Ernakulam'),
    ('Idukki', 'Idukki'),
    ('Kannur', 'Kannur'),
    ('Kasaragod', 'Kasaragod'),
    ('Kollam', 'Kollam'),
    ('Kottayam', 'Kottayam'),
    ('Kozhikode', 'Kozhikode'),
    ('Malappuram', 'Malappuram'),
    ('Palakkad', 'Palakkad'),
    ('Pathanamthitta', 'Pathanamthitta'),
    ('Thiruvananthapuram', 'Thiruvananthapuram'),
    ('Thrissur', 'Thrissur'),
    ('Wayanad', 'Wayanad'),
)

data=(
        ('Ambalappuzha South', 'Ambalappuzha South'),
        ('Chennithala', 'Chennithala'),
        ('Edathua', 'Edathua'),
        ('Karthikappally', 'Karthikappally'),
        ('Kuttanadu', 'Kuttanadu'),
        ('Mavelikkara', 'Mavelikkara'),
        ('Muthukulam', 'Muthukulam'),
        ('Pulinkunnu', 'Pulinkunnu'),
        ('Thrikkunnapuzha', 'Thrikkunnapuzha'),
        ('Veliyanad', 'Veliyanad'),
        ('Alangad', 'Alangad'),
        ('Chendamangalam', 'Chendamangalam'),
        ('Cheranallur', 'Cheranallur'),
        ('Elanji', 'Elanji'),
        ('Kadamakkudy', 'Kadamakkudy'),
        ('Kadungalloor', 'Kadungalloor'),
        ('Kanayannur', 'Kanayannur'),
        ('Koothattukulam', 'Koothattukulam'),
        ('Mulanthuruthy', 'Mulanthuruthy'),
        ('Palluruthy', 'Palluruthy'),
        ('Adimaly', 'Adimaly'),
        ('Devikulam', 'Devikulam'),
        ('Elappara', 'Elappara'),
        ('Kattappana', 'Kattappana'),
        ('Nedumkandam', 'Nedumkandam'),
        ('Peerumedu', 'Peerumedu'),
        ('Thodupuzha', 'Thodupuzha'),
        ('Udumbanchola', 'Udumbanchola'),
        ('Idukki', 'Idukki'),
        ('Vandiperiyar', 'Vandiperiyar'),
        ('Alakode', 'Alakode'),
        ('Cherukunnu', 'Cherukunnu'),
        ('Eramam', 'Eramam'),
        ('Irikkur', 'Irikkur'),
        ('Kadirur', 'Kadirur'),
        ('Kanhirode', 'Kanhirode'),
        ('Kannur', 'Kannur'),
        ('Kuthuparamba', 'Kuthuparamba'),
        ('Mattool', 'Mattool'),
        ('Pappinisseri', 'Pappinisseri'),
        ('Chandera', 'Chandera'),
        ('Kumbala', 'Kumbala'),
        ('Nileshwar', 'Nileshwar'),
        ('Uduma', 'Uduma'),
        ('Hosdurg', 'Hosdurg'),
        ('Manjeshwaram', 'Manjeshwaram'),
        ('Vellarikundu', 'Vellarikundu'),
        ('Badiyadka', 'Badiyadka'),
        ('Kanhangad', 'Kanhangad'),
        ('Periya', 'Periya'),
        ('Anchal', 'Anchal'),
        ('Chadayamangalam', 'Chadayamangalam'),
        ('Chathannoor', 'Chathannoor'),
        ('Karunagappally', 'Karunagappally'),
        ('Kottarakkara', 'Kottarakkara'),
        ('Kulakkada', 'Kulakkada'),
        ('Pathanapuram', 'Pathanapuram'),
        ('Punalur', 'Punalur'),
        ('Sasthamcotta', 'Sasthamcotta'),
        ('Vettikkavala', 'Vettikkavala'),
        ('Changanassery', 'Changanassery'),
        ('Ettumanoor', 'Ettumanoor'),
        ('Kanjirappally', 'Kanjirappally'),
        ('Kottayam', 'Kottayam'),
        ('Meenachil', 'Meenachil'),
        ('Pala', 'Pala'),
        ('Vaikom', 'Vaikom'),
        ('Vazhoor', 'Vazhoor'),
        ('Vazhappally', 'Vazhappally'),
        ('Veliyannoor', 'Veliyannoor'),
        ('Chathamangalam', 'Chathamangalam'),
        ('Koduvally', 'Koduvally'),
        ('Koyilandy', 'Koyilandy'),
        ('Kunnamangalam', 'Kunnamangalam'),
        ('Kuruvattoor', 'Kuruvattoor'),
        ('Madavoor', 'Madavoor'),
        ('Mavoor', 'Mavoor'),
        ('Perumanna', 'Perumanna'),
        ('Thikkodi', 'Thikkodi'),
        ('Thuneri', 'Thuneri'),
        ('Angadippuram', 'Angadippuram'),
        ('Edavanna', 'Edavanna'),
        ('Kalikavu', 'Kalikavu'),
        ('Kondotty', 'Kondotty'),
        ('Malappuram', 'Malappuram'),
        ('Mankada', 'Mankada'),
        ('Nilambur', 'Nilambur'),
        ('Perinthalmanna', 'Perinthalmanna'),
        ('Tirur', 'Tirur'),
        ('Tirurangadi', 'Tirurangadi'),
        ('Alathur', 'Alathur'),
        ('Chittur', 'Chittur'),
        ('Kollengode', 'Kollengode'),
        ('Mannarkkad', 'Mannarkkad'),
        ('Nemmara', 'Nemmara'),
        ('Ottappalam', 'Ottappalam'),
        ('Pattambi', 'Pattambi'),
        ('Shoranur', 'Shoranur'),
        ('Thrithala', 'Thrithala'),
        ('Palakkad', 'Palakkad'),
        ('Adoor', 'Adoor'),
        ('Kozhencherry', 'Kozhencherry'),
        ('Ranni', 'Ranni'),
        ('Konni', 'Konni'),
        ('Mallappally', 'Mallappally'),
        ('Thiruvalla', 'Thiruvalla'),
        ('Aranmula', 'Aranmula'),
        ('Pandalam', 'Pandalam'),
        ('Pathanamthitta', 'Pathanamthitta'),
        ('Vadasserikkara', 'Vadasserikkara'),
        ('Aryanad', 'Aryanad'),
        ('Nedumangad', 'Nedumangad'),
        ('Varkala', 'Varkala'),
        ('Neyyattinkara', 'Neyyattinkara'),
        ('Perumkadavila', 'Perumkadavila'),
        ('Vamanapuram', 'Vamanapuram'),
        ('Kattakada', 'Kattakada'),
        ('Vilappil', 'Vilappil'),
        ('Chirayinkeezhu', 'Chirayinkeezhu'),
        ('Poovar', 'Poovar'),
        ('Chavakkad', 'Chavakkad'),
        ('Kunnamkulam', 'Kunnamkulam'),
        ('Wadakkanchery', 'Wadakkanchery'),
        ('Irinjalakuda', 'Irinjalakuda'),
        ('Mukundapuram', 'Mukundapuram'),
        ('Chalakudy', 'Chalakudy'),
        ('Kodungallur', 'Kodungallur'),
        ('Guruvayur', 'Guruvayur'),
        ('Manalur', 'Manalur'),
        ('Mala', 'Mala'),

        ('Ambalavayal', 'Ambalavayal'),
        ('Bathery', 'Bathery'),
        ('Kaniyambatta', 'Kaniyambatta'),
        ('Kottathara', 'Kottathara'),
        ('Mananthavady', 'Mananthavady'),
        ('Meppadi', 'Meppadi'),
        ('Mullankolli', 'Mullankolli'),
        ('Nenmeni', 'Nenmeni'),
        ('Padinjarathara', 'Padinjarathara'),
        ('Pulpally', 'Pulpally'),
    
)




GENDER_CHOICES = (
    ('','') ,
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other'),
    )
NOTI_CHOICES = (
    ('','') ,
    ('ADS', 'ADS'),
    ('PUBLIC', 'PUBLIC'),
    ('EMPLOYEE','EMPLOYEE') ,
    )

class pub1(forms.ModelForm):
    class Meta:
        model=pub
        fields=['name','district', 'panchayath','contact','emailid','password']

        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'district': forms.Select(attrs={'class': 'form-control'}),
            'panchayath': forms.Select(attrs={'class': 'form-control', 'id': 'id_panchayath_name'}),
            'contact':forms.TextInput(attrs={'class':'form-control'}),
            'emailid':forms.TextInput(attrs={'class':'form-control'}),
            'password':forms.TextInput(attrs={'class':'form-control'}),
        }

    district = forms.ChoiceField(
        label='Panchayath District',
        choices=KERALA_DISTRICTS,
        widget=forms.Select(attrs={'class': 'form-control'}))
    panchayath =  forms.ChoiceField(
        label='Panchayath',
        choices=data,
        widget=forms.Select(attrs={'class': 'form-control'}))

    def clean_contact(self):
        contact = str(self.cleaned_data['contact'])
        if not re.match(r'^\d{10}$',contact):
            raise ValidationError("Invalid contact number. Please enter a 10-digit phone number.")

        return contact
    def clean_password(self):
        password = self.cleaned_data.get('password')

        # Password validation rules (customize as needed)
        if len(password) < 8:
            raise ValidationError("Password must be at least 8 characters long.")
        if not any(char.isdigit() for char in password):
            raise ValidationError("Password must contain at least one digit.")
        if not any(char.isalpha() for char in password):
            raise ValidationError("Password must contain at least one letter.")

        return password

    # def clean_emailid(self):
    #     email = self.cleaned_data['emailid']
    #     if pub.objects.filter(emailid=email).exists():
    #         raise ValidationError("This email address is already registered.")
    #     return email

    def _init_(self, *args, **kwargs):
        super()._init_(*args, **kwargs)
        if kwargs.get('instance'):
            self.fields['emailid'].widget.attrs['readonly']=True

class panchayath1(forms.ModelForm):
    class Meta:
        model=panchayath
        fields=['panchayath_district','panchayath_name','panchayath_address','panchayath_city','panchayath_pincode','panchayath_contact','panchayath_email','panchayath_password']
    widgets={
        'panchayath_district':forms.Select(attrs={'class': 'form-control'}),
        'panchayath_name': forms.Select(attrs={'class': 'form-control', 'id': 'id_panchayath_name'}),
        'panchayath_address':forms.TextInput(attrs={'class':'form-control'}),
        'panchayath_city':forms.TextInput(attrs={'class':'form-control'}),
        'panchayath_pincode':forms.TextInput(attrs={'class':'form-control'}),
        'panchayath_contact':forms.TextInput(attrs={'class':'form-control'}),
        'panchayath_email':forms.TextInput(attrs={'class':'form-control'}),
        'panchayath_password':forms.TextInput(attrs={'class':'form-control'}),
    }
    panchayath_district = forms.ChoiceField(
        label='Panchayath District',
        choices=KERALA_DISTRICTS,
        widget=forms.Select(attrs={'class': 'form-control'}))
    panchayath_name =  forms.ChoiceField(
        label='Employee Panchayath',
        choices=data,
        widget=forms.Select(attrs={'class': 'form-control'}))
    panchayath_address = forms.CharField(label='Panchayath Address',widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    panchayath_city = forms.CharField(label='Panchayath City',widget=forms.TextInput(attrs={'class': 'form-control'}))
    panchayath_pincode = forms.CharField(label='Panchayath Pincode',widget=forms.TextInput(attrs={'class': 'form-control'}))
    panchayath_contact = forms.CharField(label='Panchayath Contact',widget=forms.TextInput(attrs={'class': 'form-control'}))
    panchayath_email = forms.CharField(label='Panchayath Email',widget=forms.TextInput(attrs={'class': 'form-control'}))
    panchayath_password = forms.CharField(label='Panchayath Password', widget=forms.TextInput(attrs={'class': 'form-control'}))

    def clean_panchayath_contact(self):
        panchayath_contact = str(self.cleaned_data['panchayath_contact'])
        if not re.match(r'^\d{10}$',panchayath_contact):
            raise ValidationError("Invalid contact number. Please enter a 10-digit phone number.")

        return panchayath_contact

    def clean_panchayath_password(self):
        panchayath_password = self.cleaned_data.get('panchayath_password')

        # Password validation rules (customize as needed)
        if len(panchayath_password) < 8:
            raise ValidationError("Password must be at least 8 characters long.")
        if not any(char.isdigit() for char in panchayath_password):
            raise ValidationError("Password must contain at least one digit.")
        if not any(char.isalpha() for char in panchayath_password):
            raise ValidationError("Password must contain at least one letter.")

        return panchayath_password

    def clean_panchayath_pincode(self):
        panchayath_pincode = self.cleaned_data['panchayath_pincode']
        if not (len(panchayath_pincode) == 6 or len(panchayath_pincode) == 7) or not panchayath_pincode.isdigit():
            raise ValidationError("Invalid pincode. Please enter a 6 or 7-digit number.")

        return panchayath_pincode

    

    

    def _init_(self, *args, **kwargs):
        super()._init_(*args, **kwargs)
        if kwargs.get('instance'):
            self.fields['panchayath_email'].widget.attrs['readonly']=True

class ads1(forms.ModelForm):
    class Meta:
        model=ads
        fields=['adsname','adsgender','adsadharno','adsdistrict','adspanchayath','adsward','adscontact','adsemail','adspassword']
        widgets={
            
            'adsname':forms.TextInput(attrs={'class':'form-control'}),
            'adsgender':forms.Select(attrs={'class': 'form-control'}),
            'adsadharno':forms.TextInput(attrs={'class':'form-control'}),
            'adsdistrict': forms.Select(attrs={'class': 'form-control'}),
            'adspanchayath': forms.Select(attrs={'class': 'form-control', 'id': 'id_adspanchayath'}),  # Add 'id' attribute
            'adsward':forms.TextInput(attrs={'class':'form-control'}),
            'adscontact':forms.TextInput(attrs={'class':'form-control'}),
            'adsemail':forms.TextInput(attrs={'class':'form-control'}),
            'adspassword':forms.TextInput(attrs={'class':'form-control'}),
        }
    adsname = forms.CharField(label='Name', widget=forms.TextInput(attrs={'class': 'form-control'}))
    adsgender = forms.ChoiceField(
        label='Gender',  # Updated label
        choices=GENDER_CHOICES,  # Assuming GENDER_CHOICES is defined in your model
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    adsadharno = forms.CharField(label='Aadhar Number', widget=forms.TextInput(attrs={'class': 'form-control'}))
    adsdistrict=forms.ChoiceField(
        label='Panchayath District',
        choices=KERALA_DISTRICTS,
        widget=forms.Select(attrs={'class': 'form-control'}))
    adspanchayath = forms.ChoiceField(
        label='ADS Panchayath',
        choices=data,
        widget=forms.Select(attrs={'class': 'form-control'}))
    adsward = forms.CharField(label='Ward', widget=forms.TextInput(attrs={'class': 'form-control'}))
    adscontact = forms.CharField(label='Contact', widget=forms.TextInput(attrs={'class': 'form-control'}))
    adsemail = forms.CharField(label='Email', widget=forms.TextInput(attrs={'class': 'form-control'}))
    adspassword = forms.CharField(label='Password', widget=forms.TextInput(attrs={'class': 'form-control'}))

    def clean_adscontact(self):
        adscontact = str(self.cleaned_data['adscontact'])
        if not re.match(r'^\d{10}$',adscontact):
            raise ValidationError("Invalid contact number. Please enter a 10-digit phone number.")

        return adscontact

    def clean_adspassword(self):
        adspassword = self.cleaned_data.get('adspassword')

        # Password validation rules (customize as needed)
        if len(adspassword) < 8:
            raise ValidationError("Password must be at least 8 characters long.")
        if not any(char.isdigit() for char in adspassword):
            raise ValidationError("Password must contain at least one digit.")
        if not any(char.isalpha() for char in adspassword):
            raise ValidationError("Password must contain at least one letter.")

        return adspassword
        
    def clean_adsadharno(self):
        adsadharno = str(self.cleaned_data['adsadharno'])
        if not re.match(r'^\d{12}$',adsadharno):
            raise ValidationError("Invalid Adhar No. Please enter a 12-digit Adhar number.")

        return adsadharno

    # def clean_adsemail(self):
    #     email = self.cleaned_data['adsemail']
    #     if ads.objects.filter(adsemail=email).exists():
    #         raise ValidationError("This email address is already registered.")
    #     return email


    def clean_adspanchayath(self):
        adspanchayath = self.cleaned_data['adspanchayath']
        # Convert the name to capital letters
        adspanchayath = adspanchayath.upper()
        return adspanchayath

    def _init_(self, *args, **kwargs):
        super()._init_(*args, **kwargs)
        if kwargs.get('instance'):
            self.fields['adsemail'].widget.attrs['readonly']=True

    def clean_adsward(self):
        adsward = self.cleaned_data['adsward']

        # Check if the value contains only digits
        if not re.match(r'^\d+$', adsward):
            raise ValidationError("Ward must contain only numbers.")

        return adsward









class workre(forms.ModelForm):
    class Meta:
        model = workrequest
        fields = ['address','district', 'panchayath', 'wardno', 'rationcardno', 'taxno','land_tax_receipt', 'area']
        widgets = {
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'district': forms.Select(attrs={'class': 'form-control'}),
            'panchayath': forms.Select(attrs={'class': 'form-control', 'id': 'id_panchayath_name'}),
            'wardno': forms.TextInput(attrs={'class': 'form-control'}),
            'rationcardno': forms.TextInput(attrs={'class': 'form-control'}),
            
            'taxno': forms.TextInput(attrs={'class': 'form-control'}),
            'area': forms.TextInput(attrs={'class': 'form-control'}),
        }

    district = forms.ChoiceField(
        label='Panchayath District',
        choices=KERALA_DISTRICTS,
        widget=forms.Select(attrs={'class': 'form-control'}))
    panchayath =  forms.ChoiceField(
        label='Panchayath',
        choices=data,
        widget=forms.Select(attrs={'class': 'form-control'}))
    def clean_rationcardno(self):
        rationcardno = str(self.cleaned_data['rationcardno'])
        if not re.match(r'^\d{10}$',rationcardno):
            raise ValidationError("Invalid Ration Card No. Please enter a 10-digit Ration Card No.")

        return rationcardno

    def clean_taxno(self):
        taxno = self.cleaned_data['taxno']
        # Define a regular expression pattern for the taxno field
        taxno_pattern = r'^KL\d{14}/\d{4}$'

        if not re.match(taxno_pattern, taxno):
            raise ValidationError("Invalid tax number. It should be in the format KL<14 digit>/<Year>.")
        
        return taxno
    def clean_wardno(self):
        wardno = self.cleaned_data['wardno']

        # Check if the value contains only digits
        if not re.match(r'^\d+$', wardno):
            raise ValidationError("Ward must contain only numbers.")

        return wardno

class notifi(forms.ModelForm):
    class Meta:
        model=notifition
        fields=['notification','user']
        widgets={
            'notification':forms.Textarea(attrs={'class':'form-control'}),
            'user':forms.Select(attrs={'class': 'form-control'}),
        }
    notification = forms.CharField(label='notification', widget=forms.TextInput(attrs={'class': 'form-control'}))
    user =forms.ChoiceField(
        label='user',
        choices=NOTI_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

class worken(forms.ModelForm):
    class Meta:
        model=entry12
        fields=['workdetails','startingdate','no_of_days']
        widgets={
            'workdetails':forms.TextInput(attrs={'class':'form-control'}),
            'startingdate':forms.TextInput(attrs={'class':'form-control'}),
            'no_of_days':forms.TextInput(attrs={'class':'form-control'}),
            }

    def clean_no_of_days(self):
        no_of_days = self.cleaned_data['no_of_days']

        # Convert the input to an integer
        try:
            no_of_days = int(no_of_days)
        except ValueError:
            raise ValidationError("No. of days must be a valid number.")

        # Check if the value is within the specified range
        if not (1 <= no_of_days <= 101):
            raise ValidationError("No. of days must be between 1 and 101.")

        return str(no_of_days)  # Convert it back to a string for saving to the model


class workcom(forms.ModelForm):
    class Meta:
        model=workcomplete
        fields=['completeworkdetails','currentdetails']
        widgets={
    
            'completeworkdetails':forms.TextInput(attrs={'class':'form-control'}),
            'currentdetails':forms.TextInput(attrs={'class':'form-control'}),
        }
class complain(forms.ModelForm):
    class Meta:
        model=complaints
        fields=['subject','complaint']
        widgets={
        'subject':forms.TextInput(attrs={'class':'form-control'}),
        'complaint':forms.TextInput(attrs={'class':'form-control'}),
        }
class repl(forms.ModelForm):
    class Meta:
        model=reply2
        fields=['reply']
        Widgets={
            'reply':forms.TextInput(attrs={'class':'form-control'}),
        }


class LoginForm(forms.ModelForm):
    class Meta:
       model=user
       fields=['email','password']
       widgets={
         'email':forms.TextInput(attrs={'class':'form-control'}),
         'password':forms.PasswordInput(attrs={'class':'form-control'})
       }

class takeattendence(forms.ModelForm):
    class Meta:
        model=empattendence
        fields=['attendence']

        
class newemp(forms.ModelForm):
    class Meta:
       model=newwork
       fields=['fullname','age','gender','adharno','district','panchayath','contactno',]
       widgets={
         'fullname':forms.TextInput(attrs={'class':'form-control'}),
         'age':forms.TextInput(attrs={'class':'form-control'}),
         'gender':forms.Select(attrs={'class': 'form-control'}),
         'adharno':forms.TextInput(attrs={'class':'form-control'}),
         'district':forms.Select(attrs={'class': 'form-control'}),
         'panchayath': forms.Select(attrs={'class': 'form-control', 'id': 'id_panchayath_name'}),
         'contactno':forms.TextInput(attrs={'class':'form-control'}),
       }

    district = forms.ChoiceField(
        label='Panchayath District',
        choices=KERALA_DISTRICTS,
        widget=forms.Select(attrs={'class': 'form-control'}))
    panchayath =  forms.ChoiceField(
        label='Panchayath',
        choices=data,
        widget=forms.Select(attrs={'class': 'form-control'}))

    def clean_adharno(self):
        adharno = str(self.cleaned_data['adharno'])
        if not re.match(r'^\d{12}$',adharno):
            raise ValidationError("Invalid Adhar No. Please enter a 12-digit Adhar number.")

        return adharno

    def clean_contactno(self):
        contactno = str(self.cleaned_data['contactno'])
        if not re.match(r'^\d{10}$',contactno):
            raise ValidationError("Invalid contact number. Please enter a 10-digit phone number.")

        return contactno
    
    def clean_age(self):
        age = str(self.cleaned_data['age'])

        # Check if the value contains only digits
        if not re.match(r'^\d+$', age):
            raise ValidationError("Age must contain only numbers.")

        return age

class feed(forms.ModelForm):
    class Meta:
        model=feedbacks
        fields=['feedback']
        widgets={
        'feedback':forms.Textarea(attrs={'class':'form-control'}),
        }

class salary12(forms.ModelForm):
    class Meta:
        model=salary
        fields=['name_of_cardholder','amount','card_number','cvv','card_expiry',]
        widgets={
            'name_of_cardholder':forms.TextInput(attrs={'class':'form-control'}),
            'amount':forms.TextInput(attrs={'class':'form-control'}),
            'card_number':forms.TextInput(attrs={'class':'form-control'}),
            'cvv':forms.TextInput(attrs={'class':'form-control'}),
            'card_expiry':forms.TextInput(attrs={'class':'form-control'}),
    
        }

    def clean_amount(self):
        amount = self.cleaned_data['amount']
        if amount is not None and amount <= 0:
            raise ValidationError("Amount must be a positive number.")
        return amount

    def clean_card_number(self):
        card_number = self.cleaned_data['card_number']
    
    # Check for card number validation rules
        if card_number is not None:
            card_number_str = str(card_number)  # Convert to a string to count digits
            if len(card_number_str) != 16 or not card_number_str.isdigit():
                raise ValidationError("Card number must be a 16-digit positive number.")
    
        return card_number



    def clean_cvv(self):
        cvv = self.cleaned_data['cvv']
    
    # Check for CVV validation rules
        if cvv is not None:
            cvv_str = str(cvv)  # Convert to a string to count digits
            if len(cvv_str) != 3 or not cvv_str.isdigit():
                raise ValidationError("CVV must be a 3-digit positive number.")
    
        return cvv


    def clean_card_expiry(self):
        card_expiry = self.cleaned_data['card_expiry']

    # Define a regular expression pattern for a valid date format (MM/YY)
        date_pattern = r'^(0[1-9]|1[0-2])/(\d{2})$'

    # Check if the card_expiry matches the pattern
        if not re.match(date_pattern, card_expiry):
            raise ValidationError("Card expiry must be in the format MM/YY.")

    # Extract month and year from the input
        month, year = map(int, card_expiry.split('/'))
    
    # Get the current month and year
        current_month = datetime.now().month
        current_year = datetime.now().year % 100  # Get the last two digits of the current year

    # Compare with the current month and year
        if year < current_year or (year == current_year and month < current_month):
            raise ValidationError("Card expiry must be in the future.")

        return card_expiry 

class chat1(forms.ModelForm):
    class Meta:
        model=message1
        fields=['message']
        widgets={
            'message':forms.TextInput(attrs={'class':'form-control'})
        }

class rep1(forms.ModelForm):
    class Meta:
        model=reply12
        fields=['reply']
        widgets={
            'reply':forms.TextInput(attrs={'class':'form-control'})
        }


