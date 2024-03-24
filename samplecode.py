import streamlit as st
import streamlit.components.v1 as com

com.html("""
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta http-equiv="X-UA-Compatible" content="IE=edge" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>Speech2Vision</title>
    </head>
  <body>
    <!-- nav section start -->
    <nav class="nav-container">
      <div class="nav-center wrapper">
        <div class="logo-section">
          <a href="#home-section"
            ><img
              src="../images/Ear love.png"
              alt="university logo"
              class="logo"
          /></a>
        </div>
        <div class="hamburger">
          <img src="../icons/bars.svg" alt="sidebar button" />
        </div>
        <div class="nav-links-main">
          <ul class="nav-links">
            <li><a class="nav-link" href="#home-section">Home</a></li>
            <li><a class="nav-link" href="#about-section">about</a></li>
            <li><a class="nav-link" href="#feature-section">tools</a></li>
            <li><a class="nav-link" href="#contact-section">contact</a></li>
          </ul>
        </div>
      </div>
    </nav>
    <!-- nav section end -->

    <!-- sidebar section start -->
    <aside class="sidebar-container">
      <div class="sidebar-center wrapper">
        <div class="side-header">
          <div class="logo-section">
            <a href="#home-section"
              ><img
                src="../images/Ear love.png"
                alt="university logo"
                class="logo"
            /></a>
          </div>
          <div class="close-button">
            <img src="../icons/close.svg" alt="sidebar close" />
          </div>
        </div>
        <div class="sidebar-content">
          <div class="sidebar-links-main paddingTopMobile-fifty">
            <ul class="sidebar-links">
              <li><a class="nav-link active" href="#">Home</a></li>
              <li><a class="nav-link" href="#">about</a></li>
              <li><a class="nav-link" href="#">Tools</a></li>
              <li><a class="nav-link" href="#">contact</a></li>
            </ul>
          </div>
        </div>
      </div>
    </aside>
    <!-- sidebar section end -->

    <!-- home hero section start -->
    <div id="home-section" class="home-page page-hero-container">
      <div class="page-hero">
        <div class="hero-img-component">
          <div class="img-container">
            <img
              src="../images/sounds.jpg"
              alt="home page hero image"
            />
          </div>
        </div>
        <div
          class="hero-box paddingTopMobile-thirty paddingBottomMobile-thirty"
        >
          <div class="hero-content wrapper text-container text-center">
            <h1 class="heading">Visual Voices: Turn your Speech into Visual Stories</h1>
            <p class="desc">
                Empowering the deaf
            </p>
            <div class="button-container">
              <a
                href="./speech2video.html"
                target="_blank"
                class="home-button button-primary-light display-inline-flex"
              >
                get started
              </a>
            </div>
          </div>
        </div>
      </div>
    </div>
    <!-- home hero section end -->


    <!-- single featured component start -->
    <div id="about-section" class="single-featured-container reverse-content light-blue-background">
      <div class="single-featured-center wrapper">
        <div
          class="section-title paddingTopDesktop-hundred paddingTopMobile-fifty"
        >
          <h3 class="title">about us</h3>
          <div class="underline"></div>
        </div>
        <section
          class="single-featured paddingTopDesktop-fifty paddingBottomDesktop-hundred paddingTopMobile-fifty paddingBottomMobile-fifty"
        >
          <div
            class="image-component single-featured-image paddingBottomMobile-fifty"
          >
            <img
              src="../images/Hero BG.jpeg"
              alt="about section featured content"
            />
          </div>
          <div class="single-featured-text-component">
            <div class="featured-center">
              <div class="about-info">
                <p>
                    Our goal is to make communication more accessible and inclusive for the deaf community. We understand the challenges faced by individuals who rely on visual communication, and we are committed to providing innovative solutions. Our tools are designed to transform spoken words into visual stories, enabling better understanding and engagement with the world.
                </p>
                <p>
                    Through our speech-to-text feature, we convert spoken language into written text, making it easier for the deaf to follow conversations. With our text-to-video service, we create engaging videos from written text, offering a richer experience of the content. Our speech-to-video option combines both features, providing dynamic visual narratives from spoken words.
                </p>
                <p>
                    Accessibility is at the core of our mission. We continuously strive to develop tools that empower the deaf community and promote inclusivity. Join us in our journey towards a more connected and accessible world."
                </p>
              </div>
            </div>
          </div>
        </section>
      </div>
    </div>
    <!-- single featured component end -->


    <!-- featured courses start -->
    <div id="feature-section" class="featured-courses-container light-blue-background">
      <div class="featured-courses-center wrapper">
        <div
          class="section-title paddingTopDesktop-hundred paddingTopMobile-fifty"
        >
          <h3 class="title">Features</h3>
          <div class="underline"></div>
        </div>
        <section
          class="featured-courses paddingTopDesktop-fifty paddingBottomDesktop-fifty paddingTopMobile-fifty paddingBottomMobile-fifty three-column-layout"
        >
          <!-- single course start -->
          <article class="single-course">
            <div class="img-container">
              <img src="../images/S2T.jpeg" alt="computer science" />
            </div>
            <div class="course-title">
              <p>
                Speech To Text
                <a
                    href="./speech2text.html"
                    target="_blank"
                    class="home-button button-primary-light"
                    >
                    Launch
                </a>
              </p>
                
        </div>
          </article>
          <!-- single course end -->
          <!-- single course start -->
          <article class="single-course">
            <div class="img-container">
              <img src="../images/T2V.jpeg" alt="computer science" />
            </div>
            <div class="course-title">
              <p>
                Text To Video
                <a
                    href="./text2video.html"
                    target="_blank"
                    class="home-button button-primary-light"
                    >
                    Launch
                </a>
            </p>
            </div>
          </article>
          <!-- single course end -->
          <!-- single course start -->
          <article class="single-course">
            <div class="img-container">
              <img src="../images/S2V.jpeg" alt="computer science" />
            </div>
            <div class="course-title">
              <p>
                Speech To Video
                <a
                    href="./speech2video.html"
                    target="_blank"
                    class="home-button button-primary-light"
                    >
                    Launch
                </a>
            </p>
            </div>
          </article>
          <!-- single course end -->
        </section>
      </div>
    </div>
    <!-- featured courses end -->

    <!-- single featured component start -->
    <div id="contact-section" class="single-featured-container light-blue-background">
        <div class="single-featured-center wrapper">
          <div
            class="section-title paddingTopDesktop-hundred paddingTopMobile-fifty"
          >
            <h3 class="title">contact us</h3>
            <div class="underline"></div>
          </div>
          <section
            class="single-featured paddingTopDesktop-fifty paddingBottomDesktop-hundred paddingTopMobile-fifty paddingBottomMobile-fifty"
          >
            <div
              class="image-component single-featured-image paddingBottomMobile-fifty"
            >
              <img
                src="../images/contact-section.jpeg"
                alt="about section featured content"
              />
            </div>
            <div class="single-featured-text-component">
              <div class="featured-center">
                <div class="about-info">
                  <form class="contact-us-form">
                    <input
                      type="text"
                      class="primary-input full-width-mobile full-width-desktop"
                      placeholder="Enter your name"
                      required
                    />
                    <input
                      type="email"
                      class="primary-input full-width-mobile full-width-desktop"
                      placeholder="Enter your email"
                      required
                    />
                    <textarea
                      name="message"
                      id="message"
                      cols="30"
                      rows="5"
                      class="primary-textarea full-width-mobile full-width-desktop"
                      placeholder="Please write your message..."
                    ></textarea>
                    <button class="button-primary-dark full-width-mobile">
                      submit
                    </button>
                  </form>
                </div>
              </div>
            </div>
          </section>
        </div>
      </div>
      <!-- single featured component end -->

    <!-- footer section start -->
    <div class="footer-container">
      <div class="footer-center wrapper">
        <div class="footer-links-main">
          <ul class="footer-links">
            <li><a class="footer-link active" href="#home-section">Home</a></li>
            <li><a class="footer-link" href="#about-section">about</a></li>
            <li><a class="footer-link" href="#feature-section">Tools</a></li>
            <li>
              <a class="footer-link" href="#contact-section">contact</a>
            </li>
          </ul>
        </div>
        <div class="social-links-main">
          <ul class="social-links">
            <li class="social-link">
              <a
                href="#"
                target="_blank"
              >
                <img src="../icons/linkedin.svg" alt="srikanth linkedin" />
              </a>
            </li>
            <li class="social-link">
              <a
                href="#"
                target="_blank"
              >
                <img src="../icons/instagram.svg" alt="srikanth instagram" />
              </a>
            </li>
            <li class="social-link">
              <a
                href="#"
                target="_blank"
              >
                <img src="../icons/youtube.svg" alt="srikanth youtube" />
              </a>
            </li>
            <li class="social-link">
              <a href="#" target="_blank">
                <img src="../icons/github.svg" alt="srikanth github" />
              </a>
            </li>
          </ul>
        </div>
        <div class="footer-copy-right">
          <p>
            Copyright 2023 - <span class="copyright-date">2024</span>, Made by Team 5B
          </p>
        </div>
      </div>
    </div>
    <!-- footer section end -->
  </body>
</html>
""")
