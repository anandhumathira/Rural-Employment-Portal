from django import forms
from . models4 import workemployee
import re
from django.core.exceptions import ValidationError
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




class emp1(forms.ModelForm):
    class Meta:
        model = workemployee
        fields = ['emname', 'emaddress', 'empincode', 'emdistrict', 'empanchayath', 'emward', 'emratiocard', 'emadhar', 'emcontact', 'emusername', 'empassword']
        widgets = {
            'emname': forms.TextInput(attrs={'class': 'form-control'}),
            'emaddress': forms.TextInput(attrs={'class': 'form-control'}),
            'empincode': forms.TextInput(attrs={'class': 'form-control'}),
            'emdistrict': forms.Select(attrs={'class': 'form-control'}),
            'empanchayath': forms.Select(attrs={'class': 'form-control'}),
            'emward': forms.TextInput(attrs={'class': 'form-control'}),
            'emratiocard': forms.TextInput(attrs={'class': 'form-control'}),
            'emadhar': forms.TextInput(attrs={'class': 'form-control'}),
            'emcontact': forms.TextInput(attrs={'class': 'form-control'}),
            'emusername': forms.TextInput(attrs={'class': 'form-control'}),
            'empassword': forms.TextInput(attrs={'class': 'form-control'}),
        }

    emname = forms.CharField(label='Employee Name', widget=forms.TextInput(attrs={'class': 'form-control'}))
    emaddress = forms.CharField(label='Employee Address', widget=forms.TextInput(attrs={'class': 'form-control'}))
    empincode = forms.CharField(label='Employee PIN Code', widget=forms.TextInput(attrs={'class': 'form-control'}))
    emdistrict = forms.ChoiceField(
        label='Employee District',
        choices=KERALA_DISTRICTS,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    empanchayath = forms.ChoiceField(
        label='Employee Panchayath',
        choices=data,
        widget=forms.Select(attrs={'class': 'form-control'}),
    )
    emward = forms.CharField(label='Employee Ward', widget=forms.TextInput(attrs={'class': 'form-control'}))
    emratiocard = forms.CharField(label='Employee Ration Card', widget=forms.TextInput(attrs={'class': 'form-control'}))
    emadhar = forms.CharField(label='Employee Aadhar', widget=forms.TextInput(attrs={'class': 'form-control'}))
    emcontact = forms.CharField(label='Employee Contact', widget=forms.TextInput(attrs={'class': 'form-control'}))
    emusername = forms.CharField(label='Employee Username', widget=forms.TextInput(attrs={'class': 'form-control'}))
    empassword = forms.CharField(label='Employee Password', widget=forms.TextInput(attrs={'class': 'form-control'}))

    def clean_emcontact(self):
        emcontact = str(self.cleaned_data['emcontact'])
        if not re.match(r'^\d{10}$',emcontact):
            raise ValidationError("Invalid contact number. Please enter a 10-digit phone number.")

        return emcontact

    def clean_empassword(self):
        empassword = self.cleaned_data.get('empassword')

        # Password validation rules (customize as needed)
        if len(empassword) < 8:
            raise ValidationError("Password must be at least 8 characters long.")
        if not any(char.isdigit() for char in empassword):
            raise ValidationError("Password must contain at least one digit.")
        if not any(char.isalpha() for char in empassword):
            raise ValidationError("Password must contain at least one letter.")
        return empassword
    
    def clean_emadhar(self):
        emadhar = str(self.cleaned_data['emadhar'])
        if not re.match(r'^\d{12}$',emadhar):
            raise ValidationError("Invalid Adhar No. Please enter a 12-digit Adhar number.")

        return emadhar

    def clean_emratiocard(self):
        emratiocard = str(self.cleaned_data['emratiocard'])
        if not re.match(r'^\d{10}$',emratiocard):
            raise ValidationError("Invalid Ration Card No. Please enter a 10-digit Ration Card No.")

        return emratiocard


    def _init_(self, *args, **kwargs):
        super()._init_(*args, **kwargs)
        if kwargs.get('instance'):
            self.fields['emusername'].widget.attrs['readonly']=True

    def clean_emward(self):
        emward = self.cleaned_data['emward']

        # Check if the value contains only digits
        if not re.match(r'^\d+$', emward):
            raise ValidationError("Ward must contain only numbers.")

        return emward
   