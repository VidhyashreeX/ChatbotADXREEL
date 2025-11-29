import streamlit as st

# Configure the page
st.set_page_config(
    page_title="Customer Service Chatbot",
    page_icon="|",
    layout="centered"
)

# Predefined questions and answers
QA_PAIRS = {
    "what are your business hours": "Our customer service is available Monday to Friday, 9:00 AM to 6:00 PM EST. We're closed on weekends and public holidays.",
    "how can i track my order": "You can track your order by logging into your account and visiting the 'My Orders' section. You'll find a tracking number there that you can use on our shipping partner's website.",
    "what payment methods do you accept": "We accept all major credit cards (Visa, Mastercard, American Express), PayPal, and bank transfers. We also offer financing options at checkout.",
    "how do i return a product": "To return a product, please follow these steps:\n1. Log in to your account\n2. Go to 'My Orders'\n3. Select the item you want to return\n4. Follow the return instructions\n5. Package the item securely\n6. Attach the return label and drop it off at the carrier",
    "can i change my shipping address": "You can change your shipping address before your order is processed. Please contact our customer service immediately with your order number and the new address. Once the order is shipped, we cannot change the delivery address.",
    "what is your return policy": "We offer a 30-day return policy. Items must be unused, in their original packaging with all tags attached. Some items may be final sale and not eligible for return.",
    "do you offer international shipping": "Yes, we ship to most countries worldwide. Shipping costs and delivery times vary by destination. You can see the shipping options and costs at checkout.",
    "how do i contact customer service": "You can reach our customer service team by:\n- Email: support@example.com\n- Phone: 1-800-123-4567\n- Live Chat: Available during business hours\n- Contact Form: Available on our website"
}

# Initialize session state for chat messages
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! I'm your customer service assistant. How can I help you today?"}
    ]

def get_response(user_input):
    """Get response based on predefined Q&A pairs"""
    user_input = user_input.lower().strip('?.,!').strip()
    
    # Check for exact matches first
    for question, answer in QA_PAIRS.items():
        if user_input == question.lower():
            return answer
    
    # Check for partial matches
    for question, answer in QA_PAIRS.items():
        if any(word in user_input.lower().split() for word in question.split()):
            return answer
    
    # Default response if no match found
    return "I'm sorry, I don't have information about that. Would you like to speak with a human representative?"

def main():
    st.title("🤖 Customer Service Assistant")
    
    # Display prebuilt questions as buttons
    st.subheader("Common Questions:")
    common_questions = list(QA_PAIRS.keys())[:6]  # Show first 6 questions as examples
    cols = st.columns(2)
    for i, question in enumerate(common_questions):
        if cols[i % 2].button(question.capitalize() + '?'):
            # Add user message to chat
            st.session_state.messages.append({"role": "user", "content": question})
            
            # Get response
            with st.spinner('Getting response...'):
                response = get_response(question)
                st.session_state.messages.append({"role": "assistant", "content": response})
            
            # Rerun to update the chat
            st.rerun()
    
    # Display chat messages
    st.write("---")
    st.subheader("Chat with us")
    
    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])
    
    # Chat input
    if prompt := st.chat_input("Type your message here..."):
        # Add user message to chat
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Display user message immediately
        with st.chat_message("user"):
            st.write(prompt)
        
        # Get response
        with st.chat_message("assistant"):
            with st.spinner('Thinking...'):
                response = get_response(prompt)
                st.write(response)
                st.session_state.messages.append({"role": "assistant", "content": response})

if __name__ == "__main__":
    main()
