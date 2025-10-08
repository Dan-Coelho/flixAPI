from django.db import models


NATIONALITY_CHOICES = (
    ("US", "United States"),
    ("UK", "United Kingdom"),
    ("CA", "Canada"),
    ("AU", "Australia"),
    ("FR", "France"),
    ("GE", "Germany"),
    ("IS", "Israel"),
    ("JP", "Japan"),
    ("BR", "Brazil"),
    ("MX", "Mexico"),
    ("IRE", "Ireland"),
    ("IT", "Italy"),
    ("ES", "Spain"),
    ("PR", "Puerto Rico"),
    ("CN", "China"),
    ("KR", "South Korea"),
    ("SE", "Sweden"),
    ("NO", "Norway"),
    ("DK", "Denmark"),
    ("FI", "Finland"),
    ("NL", "Netherlands"),
    ("BE", "Belgium"),
    ("CH", "Switzerland"),
    ("AT", "Austria"),
    ("PT", "Portugal"),
    ("GR", "Greece"),
    ("RU", "Russia"),
    ("ZA", "South Africa"),
    ("EG", "Egypt"),
    ("NG", "Nigeria"),
    ("KE", "Kenya"),
    ("AR", "Argentina"),
    ("CL", "Chile"),
    ("CO", "Colombia"),
    ("PE", "Peru"),
    ("VE", "Venezuela"),
    ("TR", "Turkey"),
    ("SA", "Saudi Arabia"),
    ("AE", "United Arab Emirates"),
    ("TH", "Thailand"),
    ("MY", "Malaysia"),
    ("SG", "Singapore"),
    ("NZ", "New Zealand"),
    # Add more countries as needed
)


class Actor(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField(null=True, blank=True)
    nationality = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        choices=NATIONALITY_CHOICES,
    )

    def __str__(self):
        return self.name
