<html>
  <div style="position: relative; overflow: hidden; padding-top: 56.25%;">
    <iframe style="position: absolute; top: 0; left: 0; right: 0; width: 100%; height: 100%; border: none;" src="https://www.youtube.com/embed/3MlalSPu1gI?rel=0&cc_load_policy=1" allowfullscreen allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share">
    </iframe>
  </div><br><br>
</html>

## Αναγνώριση εικόνας με WebUI

Για να χρησιμοποιήσεις το Ollama, πρέπει να κατεβάσεις ένα μοντέλο για να το χρησιμοποιήσεις. Προηγουμένως, χρησιμοποίησες το μοντέλο μόνο για κείμενο `gemma:2b`, αλλά σε αυτό το βήμα θα χρησιμοποιήσεις το μοντέλο ανάλυσης εικόνας που ονομάζεται `LLaVa`.

\--- task ---

Για να κατεβάσεις το μοντέλο LLaVA, απόκτησε πρόσβαση στο WebUI στη διεύθυνση `http://localhost:3000`.

\--- /task ---

\--- task ---

Εγγραφή στο WebUI του Ollama.

Όταν χρησιμοποιείς το WebUI για πρώτη φορά, θα σου ζητηθεί να δώσεις ένα όνομα, ένα email και έναν κωδικό πρόσβασης. Μπορείς να χρησιμοποιήσεις ένα οποιοδήποτε email ειδικά γι' αυτό, είναι μόνο για τοπική χρήση στο Raspberry Pi σου.

![Μια φόρμα εγγραφής για το "Open WebUI" με πεδία για όνομα, email και κωδικό πρόσβασης. Το πεδίο ονόματος συμπληρώνεται με "Mr.C", το πεδίο email με "test@whatever.com" και το πεδίο κωδικού πρόσβασης εμφανίζει μια σειρά από κουκκίδες που υποδεικνύουν έναν κρυφό κωδικό πρόσβασης. Κάτω από αυτά τα πεδία, υπάρχει ένα κουμπί "Create Account" με έναν κέρσορα που δείχνει προς αυτό και ένας σύνδεσμος για να συνδεθούν οι χρήστες που έχουν ήδη λογαριασμό.](images/webUI_signup.png)

\--- /task ---

\--- task ---

Επίλεξε ποιο μοντέλο θα χρησιμοποιήσεις από το αναπτυσσόμενο μενού στο επάνω μέρος του WebUI. Μπορείς επίσης να αναζητήσεις και να προσθέσεις νέα μοντέλα με αυτόν τον τρόπο — πληκτρολόγησε `llava:latest` στην αναζήτηση και επίλεξε `Pull llava:latest from Ollama.com`. Το μοντέλο σου θα ξεκινήσει να κατεβαίνει.

![Ένα αναπτυσσόμενο μενού με τον τίτλο "Select a model" εμφανίζει ένα πεδίο αναζήτησης με το κείμενο "llava:latest" που έχει εισαχθεί. Κάτω από το πεδίο αναζήτησης, εμφανίζεται το κείμενο "No results found", ακολουθούμενο από μια επιλογή που μπορείς να επιλέξεις "Pull 'llava:latest' from Ollama.com". Ένας κέρσορας πάνω από αυτήν την επιλογή.](images/model_dropdown.png)

\--- /task ---

\--- task ---

Περίμενε να ολοκληρωθεί η λήψη του μοντέλου και να το επαληθεύσεις. Αυτό μπορεί να διαρκέσει κάποιο χρόνο.

\--- /task ---

### Χρησιμοποίησε το LLaVa για να αναλύσεις μια εικόνα

<html>
<br><br>
  <div style="position: relative; overflow: hidden; padding-top: 56.25%;">
    <iframe style="position: absolute; top: 0; left: 0; right: 0; width: 100%; height: 100%; border: none;" src="https://www.youtube.com/embed/ruU6KsVyxKA?rel=0&cc_load_policy=1" allowfullscreen allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share">
    </iframe>
  </div><br><br>
</html>

\--- task ---

Μόλις ολοκληρωθεί η λήψη του μοντέλου LLaVA, ξεκίνησε μια νέα συνεδρία συνομιλίας επιλέγοντας το μοντέλο από τις διαθέσιμες επιλογές.

![Στιγμιότυπο που δείχνει το μενού επιλογής μοντέλου με τονισμένο το "llava:latest 7B"](images/select_llava_model.png)

\--- /task ---

\--- task ---

Ανέβασε μια εικόνα χρησιμοποιώντας το κουμπί "Upload Image".
![Ένα στοιχείο διεπαφής χρήστη με δύο κουμπιά: "Upload Files" στο επάνω μέρος με ένα εικονίδιο εγγράφου και ένα κουμπί "Send a Message" από κάτω, το οποίο είναι γκριζαρισμένο και περιλαμβάνει ένα σύμβολο συν. Ένας κέρσορας δείχνει προς το σύμβολο συν στο κουμπί "Send a Message".](images/upload_image.png)

\--- /task ---

\--- task ---

Μετά τη μεταφόρτωση, δώσε μια προτροπή ή ερώτηση σχετικά με την εικόνα στο πλαίσιο συνομιλίας. Πάτα <kbd>Enter</kbd>.

![Μια μικρή εικόνα μιας χνουδωτής πορτοκαλί γάτας με λευκό στήθος και ροζ φιόγκο γύρω από το λαιμό της. Η γάτα κοιτάζει απευθείας στην κάμερα με μια περίεργη έκφραση. Δίπλα στην εικόνα, υπάρχει ένα σύμβολο συν και το κείμενο "describe this picture".](images/cat_prompt.png)

\--- /task ---

\--- task ---

Επανεξέτασε την περιγραφή ή την ανάλυση που δημιουργήθηκε από το μοντέλο LLaVA. Μπορείς να κάνεις περισσότερες ερωτήσεις ή να ανεβάσεις επιπλέον εικόνες.

Χρησιμοποιώντας αυτήν την εικόνα:
![Η εικόνα δείχνει ένα κοντινό πλάνο μιας σπιτικής κοντότριχης γάτας με εντυπωσιακά μεγάλα μάτια και μια προσεκτική έκφραση. Η γάτα έχει αφράτο γούνινο τρίχωμα, κυρίως σε αποχρώσεις κρεμ και λευκού, με πιο σκούρα σημάδια στο πρόσωπο, στα αυτιά και στα πόδια της. Φαίνεται να κάθεται ή να είναι ξαπλωμένη, με τα μπροστινά της πόδια ελαφρώς τεντωμένα προς τον θεατή. Η ουρά της γάτας είναι τυλιγμένη πάνω στο σώμα της. Πίσω από τη γάτα υπάρχει ένα μπουκέτο από άνθη λεβάντας, που προσθέτουν μια πινελιά χρώματος και υφής στην εικόνα. Στην αριστερή πλευρά της φωτογραφίας υπάρχει μια μωβ απόχρωση, που υποδηλώνει ένα μπλε τοίχο ή φόντο. Σε πρώτο πλάνο, διακρίνεται μια ξύλινη επιφάνεια, πιθανώς ένα τραπέζι ή ένας πάγκος, με μερικά βότανα τοποθετημένα σε ένα δοχείο στην επάνω δεξιά γωνία. Το συνολικό στυλ της εικόνας είναι ρεαλιστικό με έμφαση στη λεπτομέρεια και ένα μικρό βάθος πεδίου που αναδεικνύει τα χαρακτηριστικά της γάτας.](images/cat.jpg)

Το LLaVa παρείχε αυτή την περιγραφή:

`The image shows a close-up of a domestic shorthair cat with striking large eyes and an attentive expression. The cat has a fluffy fur coat, primarily in shades of cream and white, with darker markings on its face, ears, and paws. It appears to be sitting or laying down, with its front paws slightly extended towards the viewer. The cat's tail is coiled up against its body. Behind the cat is a bouquet of lavender flowers, adding a touch of color and texture to the image. On the left side of the photo, there is a purple hue, suggesting a blue wall or background. In the foreground, a wooden surface can be seen, possibly a table or a counter, with some herbs placed in a container on the top right corner. The overall style of the image is realistic with a focus on detail and a shallow depth of field that highlights the cat's features.`

\--- /task ---
