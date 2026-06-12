# Project Write-up

The Booking Intelligence Dashboard is an AI-powered analytics system designed to analyze operational booking data and generate actionable business insights. It integrates Supabase for backend data storage, Streamlit for interactive UI, Plotly for visualization, and OpenRouter LLM for AI-driven insights.

The system processes booking data to compute key performance indicators such as total bookings, completion rate, cancellation rate, and branch-wise performance. These metrics are visualized through an interactive dashboard that provides a clear executive overview of business operations.

The dashboard includes multiple analytical views such as booking status distribution, branch performance comparison, service tier analysis, and payment status breakdown. These visualizations help identify operational trends and performance gaps across branches and services.

A key feature of the system is its AI-powered insights engine. It uses a large language model to analyze structured booking data and generate summaries covering trends, risks, anomalies, and recommendations. This enables quick decision-making without manual analysis.

To ensure reliability, AI-generated insights are validated against raw SQL queries executed on the Supabase database. This ensures transparency and correctness of all conclusions.

The architecture is modular, separating database access, business logic, visualization, and AI processing into independent components. This improves scalability and maintainability.

Overall, this project demonstrates practical skills in data engineering, business intelligence, and AI integration, simulating a real-world analytics platform used for operational decision-making.
