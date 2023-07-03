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

