<script>
import { useToast } from 'vue-toastification';

export default {
  name: "ContactForm",
  setup() {
    const toast = useToast();
    return { toast };
  },
  data() {
    return {
      form: {
        name: "",
        email: "",
        subject: "",
        message: "",
      },
      isSubmitting: false,
    };
  },
  methods: {
    async handleSubmit() {
      this.isSubmitting = true;

      try {
        const response = await fetch("/sendmail/", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            name: this.form.name,
            email: this.form.email,
            subject: this.form.subject,
            message: this.form.message,
          }),
        });

        if (!response.ok) {
          throw new Error("Failed to send message.");
        }

        const result = await response.json();

        this.toast.success(result.message || "Your message has been sent!", {
          position: "top-right",
          timeout: 3000,
        });

        this.form = { name: "", email: "", subject: "", message: "" };
      } catch (error) {
        this.toast.error(error.message || "Something went wrong. Please try again.", {
          position: "top-right",
          timeout: 3000,
        });
      } finally {
        this.isSubmitting = false;
      }
    },
  },
};
</script>

<template>
  <div class="contact-form">
    <h2>Contact Us</h2>
    <form @submit.prevent="handleSubmit">
      <div class="form-group-name">
        <div>
          <label for="name">Name</label>
          <input type="text" id="name" v-model="form.name" required />
        </div>
        <div>
          <label for="email">Email</label>
          <input type="email" id="email" v-model="form.email" required />
        </div>
      </div>

      <div class="form-group">
        <label for="subject">Subject</label>
        <input type="text" id="subject" v-model="form.subject" required />
      </div>

      <div class="form-group">
        <label for="message">Your Message</label>
        <textarea id="message" v-model="form.message" required></textarea>
      </div>

      <button type="submit" :disabled="isSubmitting">
        {{ isSubmitting ? "Sending..." : "Send Message" }}
      </button>
    </form>
  </div>
</template>

<style scoped>
.contact-form {
  max-width: 400px;
  margin: 40px auto;
  padding: 15px;
}
.form-group-name {
  display: flex;
  gap: 10px;
  margin-bottom: 10px;
}
.form-group-name div {
  flex: 1;
}
.form-group {
  margin-bottom: 10px;
}
input, textarea {
  width: 100%;
  padding: 6px;
  border: 1px solid #ccc; /* Lighter border for visibility */
  border-radius: 4px;
  background-color: #f9f9f9; /* Slight gray background to stand out against white */
  color: #333;
  font-family: Arial, sans-serif;
  box-sizing: border-box;
}

input::placeholder,
textarea::placeholder {
  color: #999; /* Makes placeholder text visible */
  font-style: italic;
}

textarea {
  min-height: 100px;
  resize: none;
}
button {
  width: 100%;
  padding: 12px;
  background-color: var(--theme-1, #007BFF); /* Fallback blue */
  color: #fff;
  font-weight: bold;
  font-size: 1rem;
  border: none;
  border-radius: 6px;
  cursor: pointer;
  transition: background-color 0.2s ease, transform 0.1s ease;
  font-family: system-ui, Helvetica, Arial, sans-serif;
}

button:hover:not(:disabled) {
  background-color: var(--theme-3, #0056b3); /* Fallback darker blue */
  transform: translateY(-1px);
}

button:disabled {
  background-color: #ccc;
  cursor: not-allowed;
  color: #666;
}

</style>
