from django.shortcuts import render
from dashboard_for_ad_images.util import impressions_df,clicks_df
# Create your views here.
def dashboard(request):
    impressions_data=impressions_df['impressions'].tolist()
    impressions_labels=impressions_df['colors'].tolist()
    clicks_data=clicks_df['clicks'].tolist()
    clicks_colors=clicks_df['colors'].tolist()
    context={
        'imp_data':impressions_data,
        'labels_colors':impressions_labels,
        'clicks_data':clicks_data,
        'clicks_labels':clicks_colors}
    return render(request,'dashboard.html',context)
def upload_view(request):
    if request.method == 'POST':
        # Logic to process the uploaded file
        file = request.FILES.get('csv_file')
        # Perform any required operations with the file
        # For example, save the file to a specific location or process its content

        # Add a variable to the context to indicate that the file has been uploaded
        context = {'file_uploaded': True}
        return render(request, 'upload.html', context)

    return render(request, 'upload.html')
