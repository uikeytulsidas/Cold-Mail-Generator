from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Lead, GeneratedEmail
from rest_framework.views import APIView
from rest_framework import status, generics
from .serializers import LeadSerializer, GeneratedEmailSerializer
from .services.groq_service import generate_cold_email

# # Create Lead
# @api_view(["POST"])
# def create_lead(request):
#     serializer = LeadSerializer(data=request.data)
#     if serializer.is_valid():
#         lead = serializer.save()
#         return Response({"message": "Lead created", "lead": serializer.data}, status=201)
#     return Response(serializer.errors, status=400)


# # List Leads
# @api_view(["GET"])
# def list_leads(request):
#     leads = Lead.objects.all().order_by("-created_at")
#     serializer = LeadSerializer(leads, many=True)
#     return Response(serializer.data)

# @api_view(["GET"])
# def list_generated_emails(request, lead_id):
#     emails = GeneratedEmail.objects.filter(lead_id=lead_id).order_by("-created_at")
#     serializer = GeneratedEmailSerializer(emails, many=True)
#     return Response(serializer.data)



# # Generate Cold Email for a Lead
# @api_view(["POST"])
# def generate_email(request, lead_id):
#     try:
#         lead = Lead.objects.get(id=lead_id)
#     except Lead.DoesNotExist:
#         return Response({"error": "Lead not found"}, status=404)

#     # Mock cold email content (AI integration comes later 🚀)
#     content = f"Hello {lead.name}, we at {lead.company} would like to introduce our product: {lead.product}."

#     email = GeneratedEmail.objects.create(lead=lead, content=content)
#     serializer = GeneratedEmailSerializer(email)

#     return Response(serializer.data, status=201)

# Lead CRUD
class LeadListCreateView(generics.ListCreateAPIView):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer


# Generated Emails List
class GeneratedEmailListView(generics.ListAPIView):
    queryset = GeneratedEmail.objects.all()
    serializer_class = GeneratedEmailSerializer


# Generate Email for a Lead
class GenerateEmailView(APIView):
    def post(self, request, lead_id):
        try:
            lead = Lead.objects.get(id=lead_id)
        except Lead.DoesNotExist:
            return Response({"error": "Lead not found"}, status=status.HTTP_404_NOT_FOUND)

        # Dummy generator (later we’ll connect AI/LLM)
        # content = f"Hello {lead.name},\nWe at {lead.company} would like to introduce {lead.product} for your role as {lead.role}."
        
        
        content = generate_cold_email(
    recipient_name=lead.recipient_name,
    company=lead.company,
    role=lead.role,
    job_title=lead.job_title,
    applicant_name=lead.applicant_name,
    skills=lead.skills,
    portfolio=lead.portfolio,
    why_interested=lead.why_interested
)

        email = GeneratedEmail.objects.create(lead=lead, content=content)
        serializer = GeneratedEmailSerializer(email)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
      
    def get(self, request, lead_id):
        """Return all generated emails for a given lead"""
        try:
            lead = Lead.objects.get(id=lead_id)
        except Lead.DoesNotExist:
            return Response({"error": "Lead not found"}, status=status.HTTP_404_NOT_FOUND)

        emails = lead.emails.all()
        serializer = GeneratedEmailSerializer(emails, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)