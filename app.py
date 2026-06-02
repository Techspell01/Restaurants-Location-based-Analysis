import streamlit as st
import pandas as pd

st.set_page_config(page_title="Location-Based Analysis", page_icon="🌍", layout="wide")

st.title("🌍 Restaurant Location-Based Analysis Dashboard")
st.markdown("""
Explore the geographical distribution of restaurants, analyze their concentration by city or locality, and discover data-driven insights!
""")

st.sidebar.header("1. Upload Dataset")
uploaded_file = st.sidebar.file_uploader("Upload your 'Dataset.csv' file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    df = df[(df['Latitude'] != 0) & (df['Longitude'] != 0)]
    df = df.dropna(subset=['Latitude', 'Longitude'])

    st.write("---")

    st.header("📍 1. Geographical Distribution of Restaurants")
    st.markdown("Every dot represents a restaurant from the dataset mapped via its exact coordinates.")
    
    # Streamlit's st.map requires columns specifically named 'lat' and 'lon'
    map_data = df[['Latitude', 'Longitude']].rename(columns={'Latitude': 'lat', 'Longitude': 'lon'})
    st.map(map_data)
    
    st.write("---")
    st.header("🏙️ 2. Area Concentration & Statistical Analysis")
    
    grouping_choice = st.radio("Group Data By:", options=['City', 'Locality'], horizontal=True)
    
    with st.spinner(f"Analyzing data by {grouping_choice}..."):
        
        st.subheader(f"Top 10 {grouping_choice}s with Most Restaurants")
        concentration_data = df[grouping_choice].value_counts().head(10)
        st.bar_chart(concentration_data)
    
        st.subheader(f"Detailed Statistics by {grouping_choice}")
    
        df['Cuisines'] = df['Cuisines'].fillna('Unknown')
        df['Aggregate rating'] = df['Aggregate rating'].fillna(0)
        df['Price range'] = df['Price range'].fillna(1)
        
        stats_df = df.groupby(grouping_choice).agg(
            Total_Restaurants=('Restaurant Name', 'count'),
            Avg_Rating=('Aggregate rating', 'mean'),
            Avg_Price_Range=('Price range', 'mean'),
            Most_Common_Cuisine=('Cuisines', lambda x: x.mode()[0] if not x.mode().empty else 'N/A')
        ).sort_values(by='Total_Restaurants', ascending=False).reset_index()
        
        stats_df['Avg_Rating'] = stats_df['Avg_Rating'].round(2)
        stats_df['Avg_Price_Range'] = stats_df['Avg_Price_Range'].round(2)
        
        st.dataframe(stats_df, use_container_width=True)
        
    st.write("---")

    st.header(" 3. Automated Business Insights")

    top_area = stats_df.iloc[0][grouping_choice]
    top_count = stats_df.iloc[0]['Total_Restaurants']
    
    reliable_areas = stats_df[stats_df['Total_Restaurants'] >= 5]
    if not reliable_areas.empty:
        best_rated_area = reliable_areas.sort_values(by='Avg_Rating', ascending=False).iloc[0]
        most_expensive = reliable_areas.sort_values(by='Avg_Price_Range', ascending=False).iloc[0]
        
        st.success(f"""
        **Dynamically generated insights based on your dataset:**
        * **Market Dominance:** **{top_area}** is the most saturated market, hosting **{top_count}** restaurants. Competitors looking to open new branches should expect high competition here.
        * **Highest Quality (Rating):** Among areas with at least 5 restaurants, **{best_rated_area[grouping_choice]}** holds the highest average customer rating (**{best_rated_area['Avg_Rating']} / 5.0**). The primary cuisine driving this area is '{best_rated_area['Most_Common_Cuisine']}'.
        * **Premium Dining:** The most expensive area to dine in on average is **{most_expensive[grouping_choice]}**, with an average price range scale of **{most_expensive['Avg_Price_Range']}**. 
        """)
    else:
        st.warning("Not enough data to confidently generate advanced rating insights. Try uploading a larger dataset.")

else:
    st.info("👈 Please upload your 'Dataset.csv' file in the sidebar to run the geographic analysis.")