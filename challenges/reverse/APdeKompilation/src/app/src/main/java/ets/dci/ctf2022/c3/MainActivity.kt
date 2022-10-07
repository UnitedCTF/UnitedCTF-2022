package ets.dci.ctf2022.c3

import android.os.Bundle
import android.view.View
import android.widget.Button
import android.widget.EditText
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity
import ets.dci.ctf2022.c3.R


class MainActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)


        val flagName: EditText = findViewById(R.id.idFlagName)
        val btnAddCourse: Button = findViewById(R.id.idBtnAddCourse)
        val searchResult: TextView = findViewById(R.id.idSearchResult)

        btnAddCourse.setOnClickListener(object : View.OnClickListener {
            override fun onClick(v: View?) {

                // below line is to get data from all edit text fields.
                val flagName = flagName.text.toString()


                if (flagName == "FLAG-bb2aee5a1374a1a567f07d5d30db1c5b")
                    searchResult.text = "Success, this is the flag!"
                else
                    searchResult.text = "Error, the flag does not match"
            }
        })
    }
}