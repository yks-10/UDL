PAGINATION_COUNT=10

OPT_IN = 'opt_in'
OPT_OUT = 'opt_out'
COMMUNICATION_CHOICES = [
    (OPT_IN, 'Opt In'),
    (OPT_OUT, 'Opt Out'),
]

FOOD = 'food'
HOME = 'home'
REQUEST_CATEGORY = [
    (FOOD, 'Food'),
    (HOME, 'Home'),
]

TODAY = 'today'
TOMORROW = 'tomorrow'
DURATION_CHOICES = [
    (TODAY, 'Today'),
    (TOMORROW, 'Tomorrow'),
]

INTERNAL = 'internal'
EXTERNAL = 'external'
BOTH = 'both'
REQUEST_TYPE_CHOICES = [
    (INTERNAL, 'Internal'),
    (EXTERNAL, 'External'),
    (BOTH, 'Both'),
]

HIGH = 'high'
LOW = 'low'
MEDIUM = 'medium'
URGENCY_TYPE_CHOICES = [
    (HIGH, 'High'),
    (LOW, 'Low'),
    (MEDIUM, 'Medium'),
]

CALL = 'call'
WALK_IN = 'walk_in'
ONLINE = 'online'
EMAIL = 'email'
REQUEST_VIA = [
    (CALL, 'Call'),
    (WALK_IN, 'Walk In'),
    (ONLINE, 'Online'),
    (EMAIL, 'Email'),
]

MALE = 'male'
FEMALE = 'female'
OTHER = 'other'
GENDER_CHOICES = [
    (MALE, 'Male'),
    (FEMALE, 'Female'),
    (OTHER, 'Other'),
]

ONE_HOUR = 'one hour'
ONE_DAY = 'one day'
WEEK = 'week'
MONTH = 'month'
YEAR = 'year'
DELIVERY_TIME_PERIOD_CHOICES = [
    (ONE_HOUR, 'One Hour'),
    (ONE_DAY, 'One Day'),
    (WEEK, 'Week'),
    (MONTH, 'month'),
    (YEAR, 'year'),
]

ALL_DAY = 'all day'
WEEKLY = 'weekly'
MONTHLY = 'monthly'
YEARLY = 'yearly'
AVAILABLE_DAYS_CHOICES = [
    (ALL_DAY, 'All Day'),
    (ONE_DAY, 'One Day'),
    (WEEKLY, 'Weekly'),
    (MONTHLY, 'Monthly'),
    (YEARLY, 'Yearly'),
]

ZERO_FIVE = '0-5'
FIVE_TO_TEN = '5-10'
TEN_TO_FIFTEEN = '10-15'
FIFTEEN_TO_TWENTY = '15-20'
TWENTY_TO_TWENTYFIVE = '20-25'
TWENTYFIVE_TO_THIRTY = '25-30'
THIRTY_ABOVE = '30-above'
REQUEST_QUANTITY = [
    (ZERO_FIVE, '0-5'),
    (FIVE_TO_TEN, '5-10'),
    (TEN_TO_FIFTEEN, '10-15'),
    (FIFTEEN_TO_TWENTY, '15-20'),
    (TWENTY_TO_TWENTYFIVE, '20-25'),
    (TWENTYFIVE_TO_THIRTY, '25-30'),
    (THIRTY_ABOVE, '30-Above'),
]

ACTIVE = 'active'
INACTIVE = 'inactive'
ARCHIVE = 'archive'
UNARCHIVE = 'unarchive'
STATUS_CHOICES = [
    (ACTIVE, 'Active'),
    (INACTIVE, 'Inactive'),
    (ARCHIVE, 'Archive'),
    (UNARCHIVE, 'UnArchive')
]

NEW = 'new'
PENDING='pending'
IN_PROGRESS = 'in progress'
COMPLETED = 'completed'
RESOLVED = 'resolved'
CANCELLED = 'cancelled'
ON_HOLD = 'on hold'
REJECTED = 'rejected'
IN_REVIEW = 'in review'
FAILED = 'failed'
CLOSED = 'closed'
ASSIGNED = 'assigned'
REQUEST_STATUS_CHOICES = [
    (NEW, 'New'),
    (PENDING, 'Pending'),
    (IN_PROGRESS, 'In Progress'),
    (COMPLETED, 'Completed'),
    (CANCELLED, 'Cancelled'),
    (ON_HOLD, 'On Hold'),
    (REJECTED, 'Rejected'),
    (IN_REVIEW, 'In Review'),
    (FAILED, 'Failed'),
    (RESOLVED, 'Resolved'),
    (CLOSED, "Closed"),
    (ASSIGNED, "Assigned")
]

WAIT = 'wait'
ACCEPTED = 'accepted'
IMPORTANT = 'important'
PARTNER_STATUS_CHOICE = [
    (WAIT, 'Wait'),
    (NEW, 'New'),
    (IN_PROGRESS, 'In Progress'),
    (ACCEPTED, 'Accepted'),
    (ON_HOLD, 'On Hold'),
    (COMPLETED, 'Completed'),
    (CANCELLED, 'Cancelled'),
    (REJECTED, 'Rejected'),
    (IMPORTANT, 'Important'),
    (RESOLVED, 'Resolved'),
    (CLOSED, "Closed"),
    (ASSIGNED, "Assigned")
]

ACTIVE = 'active'
INACTIVE = 'inactive'
ARCHIVE = 'archive'
UNARCHIVE = 'unarchive'
DECLINED = 'declined'
NOT_ACCEPTED = 'not accepted'
DUPLICATE = 'duplicate'
DECEASED = 'deceased'
NO_LONGER = 'no longer'
DISMISSED = 'dismissed'
PENDING_ACTIVATE = 'pending activate'
STATUS_CHOICES = [
    (NEW, 'New'),
    (ARCHIVE, 'Archive'),
    (UNARCHIVE, 'UnArchive'),
    (PENDING, 'Pending'),
    (IN_REVIEW, 'In Review'),
    (ACCEPTED, 'Accepted'),
    (NOT_ACCEPTED, 'Not Accepted'),
    (DECLINED, 'Declined'),
    (ACTIVE, 'Active'),
    (INACTIVE, 'Inactive'),
    (REJECTED, 'Rejected'),
    (DUPLICATE, 'Duplicate'),
    (DECEASED, 'Deceased'),
    (NO_LONGER, 'No Longer'),
    (DISMISSED, 'Dismissed'),
    (PENDING_ACTIVATE, 'Pending Activate'),
]

WAITING = 'waiting'
UNAVAILABLE = 'unavailable'
FOLLOW_UP_STATUS_CHOICES = [
    (NEW, 'New'),
    (WAITING, 'Waiting'),
    (COMPLETED, 'Completed'),
    (UNAVAILABLE, 'Unavailable')
]

TEXT = "text"
CONTACT_VIA_CHOICES = [
    (CALL, 'CALL'),
    (TEXT, 'TEXT')
]

REGISTERED = 'registered'
UNREGISTERED = 'unregistered'
DECLINED = 'declined'

REGISTER_STATUS_CHOICES = [
    (REGISTERED, 'registered'),
    (UNREGISTERED, 'unregistered'),
    (DECLINED, 'declined')
]

MEMBERSHIP = 'membership'
EMERGENCY = 'emergency'
PARTNERSHIP = 'partnership'
GRANT = 'grant'
EVENT = 'event'
RESOURCE = 'resource'
SUPPORT = 'support'
LEGAL = 'legal'
TECHNOLOGY_SUPPORT = 'technology support'
TRAINING = 'training'
EDUCATIONAL_MATERIALS = 'educational materials'
RESEARCH_AND_DATA = 'research and data'
FACILITY_USE = 'facility use'
MEDIA_AND_PR = 'media and public relations'
SPONSORSHIP = 'sponsorship'
OFFLINE_LEARNING = 'offline learning'
PUBLIC_AWARENESS = 'public awareness'
COMMUNITY_ENGAGEMENT = 'community engagement'
ENVIRONMENTAL_SUSTAINABILITY = 'environmental sustainability'
CRISIS_INTERVENTION = 'crisis intervention'
FINANCIAL_ASSISTANCE = 'financial assistance'
TRANSPORTATION_ASSISTANCE = 'transportation assistance'
HEALTH_AND_WELLNESS = 'health and wellness'
JOB_TRAINING = 'job training and placement'
LANGUAGE_TRANSLATION = 'language translation'
ADVOCATE_REQUEST = 'advocate request'
AID_REQUEST = 'aid request'
CHILDCARE = 'childcare'
COUNSELING_REQUEST = 'counseling request'
DONATION_REQUEST = 'donation request'
HOUSING_REPAIR = 'housing repair'
JOB_TRAINING_AND_PLACEMENT = 'job training and placement'
MEDIA_AND_PUBLIC_RELATIONS = 'media and public relations'
MENTORSHIP_REQUEST = 'mentorship request'
SPORTS_AND_RECREATION = 'sports and recreation'
VOLUNTEER = 'volunteer'
CATEGORY_CHOICES = [
    (ADVOCATE_REQUEST, 'Advocate Request'),
    (AID_REQUEST, 'Aid Request'),
    (CHILDCARE, 'Childcare'),
    (COMMUNITY_ENGAGEMENT, 'Community Engagement'),
    (COUNSELING_REQUEST, 'Counseling Request'),
    (CRISIS_INTERVENTION, 'Crisis Intervention'),
    (DONATION_REQUEST, 'Donation Request'),
    (EDUCATIONAL_MATERIALS, 'Educational Materials'),
    (EMERGENCY, 'Emergency'),
    (ENVIRONMENTAL_SUSTAINABILITY, 'Environmental Sustainability'),
    (EVENT, 'Event'),
    (FACILITY_USE, 'Facility Use'),
    (FINANCIAL_ASSISTANCE, 'Financial Assistance'),
    (GRANT, 'Grant'),
    (HEALTH_AND_WELLNESS, 'Health and Wellness'),
    (HOUSING_REPAIR, 'Housing Repair'),
    (JOB_TRAINING_AND_PLACEMENT, 'Job Training and Placement'),
    (LANGUAGE_TRANSLATION, 'Language Translation'),
    (LEGAL, 'Legal'),
    (MEDIA_AND_PUBLIC_RELATIONS, 'Media and Public Relations'),
    (MEMBERSHIP, 'Membership'),
    (MENTORSHIP_REQUEST, 'Mentorship Request'),
    (OFFLINE_LEARNING, 'Offline Learning'),
    (PARTNERSHIP, 'Partnership'),
    (PUBLIC_AWARENESS, 'Public Awareness'),
    (RESEARCH_AND_DATA, 'Research and Data'),
    (RESOURCE, 'Resource'),
    (SPONSORSHIP, 'Sponsorship'),
    (SPORTS_AND_RECREATION, 'Sports and Recreation'),
    (SUPPORT, 'Support'),
    (TECHNOLOGY_SUPPORT, 'Technology Support'),
    (TRAINING, 'Training'),
    (TRANSPORTATION_ASSISTANCE, 'Transportation Assistance'),
    (VOLUNTEER, 'Volunteer'),
]


CONSUMER = 'consumer'
AGENT = 'agent'
PARTNER = 'partner'
ADMIN = 'admin'

STAFF = 'staff'
USER_CHOICES = [
    (CONSUMER, 'Consumer'),
    (AGENT, 'Agent'),
    (PARTNER, 'Partner'),
    (ADMIN, 'Admin'),
    (STAFF, 'Staff')
]

BADGE_MAP = {
    "Gold": (75, float('inf')),   # 75 to infinity
    "Silver": (50, 74),          # 50 to 74
    "Bronze": (25, 49),          # 25 to 49
    "No Badge": (0, 24),         # 0 to 24
}

AGENT = 'agent'
CATEGORY= 'category'
PARTNER = 'partner'
REQUEST = 'request'
PROFILE = 'profile'
FILE_MODULES =[
    (AGENT, 'Agent'),
    (PARTNER, 'Partner'),
    (CATEGORY, 'Category'),
    (REQUEST, 'Request'),
    (PROFILE, 'Profile'),
]

EXCLUDED_DATA_TYPES = ['line', 'character', 'json']

MONDAY = "monday"
TUESDAY = "tuesday"
WEDNESDAY = "wednesday"
THURSDAY = "thursday"
FRIDAY = "friday"
SATURDAY = "saturday"
SUNDAY = "sunday"
DAYS_OF_WEEK = [
    (MONDAY, "Monday"),
    (TUESDAY, "Tuesday"),
    (WEDNESDAY, "Wednesday"),
    (THURSDAY, "Thursday"),
    (FRIDAY, "Friday"),
    (SATURDAY, "Saturday"),
    (SUNDAY, "Sunday"),
]